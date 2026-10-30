// Integration: Füll-Liste über die Listen-Seite anlegen, Runden füllen (sicher/unsicher/nicht),
// Abschluss-Zustand, und der Füllen-Knopf auf der Detailseite (liste.html).
import { describe, it, expect, beforeEach } from 'vitest';
import { readFileSync } from 'node:fs';
import { loadScripts, repoPath } from './helpers/load.js';

function fakeStorage() {
  const d = {};
  return { getItem: (k) => (k in d ? d[k] : null), setItem: (k, v) => { d[k] = String(v); }, removeItem: (k) => { delete d[k]; } };
}

const DATA = [
  'assets/data/kanji.js', 'assets/data/vokabular.js', 'assets/data/vokabular_beispiele.js',
  'assets/data/vokabular_tags.js', 'assets/data/grammatik.js', 'assets/data/grammatik_extra.js',
  'assets/data/grammatik_furigana.js', 'assets/data/grammatik_plus.js', 'assets/data/saetze.js',
  'assets/srs.js', 'assets/exercises.js',
];

const LISTEN_BODY = `<!DOCTYPE html><html><body data-page="listen">
  <input id="lst-create-name"><button id="lst-create"></button><button id="lst-create-fill"></button>
  <button id="lst-import"></button><input type="file" id="lst-import-file" hidden>
  <p id="lst-msg"></p>
  <div id="lst-root"></div>
</body></html>`;

let win;
const $ = (s) => win.document.querySelector(s);
const $$ = (s) => [...win.document.querySelectorAll(s)];
const click = (e) => e.dispatchEvent(new win.Event('click', { bubbles: true }));
const key = (k, code) => win.document.dispatchEvent(new win.KeyboardEvent('keydown', { key: k, code: code || k, bubbles: true }));
const visible = (s) => { const e = $(s); return !!e && !e.classList.contains('hidden') && !e.closest('[hidden]'); };
const lessonVocab = (L) => win.VOKABULAR.filter((v) => L.includes(v.lesson)).length;

function pickLessons(ls) {
  click($('#lst-create-fill'));
  $$('.fs-lesson input').forEach((b) => { if (ls.includes(+b.value)) { b.checked = true; b.dispatchEvent(new win.Event('change', { bubbles: true })); } });
}

describe('Füll-Liste auf der Listen-Seite', () => {
  beforeEach(() => {
    win = loadScripts([...DATA, 'assets/app.js'], { html: LISTEN_BODY });
    win.SRS._useStorage(fakeStorage());
  });

  it('Anlegen-Dialog: Lektionen wählen, Anlegen erst dann möglich, Name automatisch', () => {
    click($('#lst-create-fill'));
    expect($('.fill-setup-overlay').hidden).toBe(false);
    expect($$('.fs-lesson').length).toBe(25);
    expect($('.fs-create').disabled).toBe(true);
    pickLessons([1, 2, 3]);
    expect($('.fs-create').disabled).toBe(false);
    expect($('.fs-sum').textContent).toContain('L1–3');
    expect($('.fs-sum').textContent).toContain(String(lessonVocab([1, 2, 3])));
    click($('.fs-create'));
    const l = win.SRS.lists()[0];
    expect(l.name).toBe('Füll-Liste L1–3');
    expect(l.fill.lessons).toEqual([1, 2, 3]);
    // Erste Runde startet direkt
    expect($('.fill-overlay').hidden).toBe(false);
    expect($('.fl-prog').textContent).toBe('Vokabel 1 / 10');
  });

  it('Runde aus dem Beispiel: 3 sicher, 3 unsicher, 4 nicht → 7 Einträge; Weiter füllen bringt neue Wörter', () => {
    pickLessons([1, 2, 3]);
    click($('.fs-create'));
    const ratings = ['sure', 'sure', 'sure', 'unsure', 'unsure', 'unsure', 'no', 'no', 'no', 'no'];
    const shown = [];
    ratings.forEach((r) => {
      shown.push($('.fl-word').textContent);
      click($('.fl-' + r));
      if (r === 'sure') {
        // sicher: keine Übersetzung, direkt weiter
        return;
      }
      // unsicher/nicht: Übersetzung + Weiter-Knopf, Bewertungsknöpfe weg
      expect(visible('.fl-answer')).toBe(true);
      expect($('.fl-de').textContent.length).toBeGreaterThan(0);
      expect(visible('.fl-rate')).toBe(false);
      expect(visible('.fl-next-wrap')).toBe(true);
      click($('.fl-next'));
    });
    expect(new Set(shown).size).toBe(10);
    expect(visible('.fl-done')).toBe(true);
    expect($('.fl-done').textContent).toContain('3 sicher');
    expect($('.fl-done').textContent).toContain('3 unsicher');
    expect($('.fl-done').textContent).toContain('4 nicht');
    expect($('.fl-done').textContent).toContain('7');
    const l = win.SRS.lists()[0];
    expect(l.items).toHaveLength(7);

    // Weiter füllen → neue Runde
    click($('.fl-more'));
    expect($('.fl-prog').textContent).toBe('Vokabel 1 / 10');
    // Schließen → Karte zeigt Füllen-Knopf und Info
    click($('.fl-close'));
    expect($('.fill-overlay').hidden).toBe(true);
    expect($('.lst-fill').textContent).toContain('Füllen fortsetzen');
    expect($('.lst-fill').textContent).toContain(String(lessonVocab([1, 2, 3]) - 10) + ' offen');
    expect($('.lst-fill-info').textContent).toContain('10 / ' + lessonVocab([1, 2, 3]));
    expect($('.lst-count').textContent).toBe('7 Einträge');
  });

  it('Tastatur: 1/2/3 bewerten, Leertaste = Weiter, Doppel-Bewertung wird ignoriert', () => {
    pickLessons([1]);
    click($('.fs-create'));
    key('3');
    key('1'); // Bewertung schon abgegeben → ignoriert
    expect(win.SRS.lists()[0].items).toHaveLength(1);
    expect($('.fl-prog').textContent).toBe('Vokabel 1 / 10');
    key(' ', 'Space');
    expect($('.fl-prog').textContent).toBe('Vokabel 2 / 10');
    key('1');
    expect($('.fl-prog').textContent).toBe('Vokabel 3 / 10');
    key('Escape');
    expect($('.fill-overlay').hidden).toBe(true);
  });

  it('wenn alles durchgegangen ist, wird Füllen gesperrt', () => {
    pickLessons([1]);
    click($('.fs-create'));
    const total = lessonVocab([1]);
    for (let i = 0; i < total; i++) {
      if (!visible('.fl-card')) click($('.fl-more'));
      click($('.fl-sure'));
    }
    expect(visible('.fl-done')).toBe(true);
    expect($('.fl-more')).toBeNull();
    expect($('.fl-all').textContent).toContain('abgeschlossen');
    click($('.fl-finish'));
    const b = $('.lst-fill');
    expect(b.disabled).toBe(true);
    expect(b.textContent).toContain('Alles durchgegangen');
    expect(win.SRS.lists()[0].items).toHaveLength(0);
  });

  it('normale Listen bekommen keinen Füllen-Knopf', () => {
    win.SRS.createList('Normal');
    win.document.getElementById('lst-create-name').value = 'Noch eine';
    click($('#lst-create'));
    expect($('.lst-fill')).toBeNull();
  });
});

describe('Füllen auf der Detailseite', () => {
  it('neu aufgenommene Einträge erscheinen ohne Neuladen', () => {
    const BODY = `<!DOCTYPE html><html><body data-page="liste">
      <h1 id="li-title"></h1><p id="li-sub"></p><div id="li-actions"></div><p id="li-msg"></p>
      <input id="search-input" type="search"><button id="toggle-readings"></button><button id="toggle-cards"></button>
      <div id="type-filters"></div><p id="count"></p><div id="content"></div><div class="empty hidden" id="empty"></div>
    </body></html>`;
    win = loadScripts(DATA, { html: BODY, url: 'https://example.test/liste.html?id=l1' });
    win.SRS._useStorage(fakeStorage());
    win.SRS.createFillList('Detail', [2]);
    const s = win.document.createElement('script');
    s.textContent = readFileSync(repoPath('assets/app.js'), 'utf8');
    win.document.head.appendChild(s);
    if (win.document.readyState === 'loading') win.document.dispatchEvent(new win.Event('DOMContentLoaded'));

    expect($('.lst-fill').textContent).toContain('Füllen starten');
    expect($('#li-sub').textContent).toContain('Füll-Liste · L2');
    click($('.lst-fill'));
    click($('.fl-no')); click($('.fl-next'));
    click($('.fl-unsure')); click($('.fl-next'));
    click($('.fl-close'));
    expect($$('#content .item').length).toBe(2);
    expect($('#li-sub').textContent).toContain('2 Einträge');
    expect($('.lst-fill').textContent).toContain('Füllen fortsetzen');
  });
});
