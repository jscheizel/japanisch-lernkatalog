// Lektionen ohne Einträge einer Art werden trotzdem gezeigt — mit Hinweis statt Lücke.
import { describe, it, expect } from 'vitest';
import { loadScripts } from './helpers/load.js';

const body = (page) => `<!DOCTYPE html><html><body data-page="${page}">
  <input id="search-input" type="search"><div id="filters"></div><div id="type-filters"></div><p id="count"></p>
  <div id="content"></div><div id="empty" class="hidden"></div></body></html>`;

function fakeStorage() {
  const d = {};
  return { getItem: (k) => (k in d ? d[k] : null), setItem: (k, v) => { d[k] = String(v); }, removeItem: (k) => { delete d[k]; } };
}
function page(name, data) {
  const win = loadScripts(data.concat(['assets/srs.js', 'assets/app.js']), { html: body(name) });
  win.SRS._useStorage(fakeStorage());
  // In jsdom ist readyState beim Skript-Append noch 'loading' → init() wartet auf DOMContentLoaded.
  if (win.document.readyState === 'loading') win.document.dispatchEvent(new win.Event('DOMContentLoaded'));
  return win;
}
function search(win, q) {
  const i = win.document.getElementById('search-input'); i.value = q;
  i.dispatchEvent(new win.Event('input', { bubbles: true }));
}
const chip = (win, val) => win.document.querySelector('#filters .chip[data-val="' + val + '"]');

describe('Leere Lektionen in den Übersichten', () => {
  it('Grammatik: L2 und L7 (ohne neue Grammatik) erscheinen mit Hinweis', () => {
    const win = page('grammatik', ['assets/data/grammatik.js', 'assets/data/grammatik_extra.js', 'assets/data/grammatik_furigana.js', 'assets/data/grammatik_plus.js']);
    const groups = [...win.document.querySelectorAll('#content .group')];
    expect(groups.length).toBe(14); // L0–13, keine fehlt
    ['2', '7'].forEach((L) => {
      const g = win.document.querySelector('.group-empty[data-empty-for="' + L + '"]');
      expect(g, 'L' + L).toBeTruthy();
      expect(g.textContent).toContain('keine neue Grammatik');
      expect(g.classList.contains('hidden')).toBe(false);
    });
    expect(chip(win, '7')).toBeTruthy(); // auch die leere Lektion hat einen Filter-Chip
  });

  it('Kanji: alle 14 Lektionen erscheinen; ohne neue Kanji steht ein Hinweis', () => {
    const win = page('kanji', ['assets/data/kanji.js']);
    expect(win.document.querySelectorAll('#content .group').length).toBe(14);
    const g = win.document.querySelector('.group-empty[data-empty-for="L1"]');
    expect(g.textContent).toContain('keine neuen Kanji');
  });

  it('Filter-Chip der leeren Lektion zeigt den Hinweis, nicht „keine Treffer"', () => {
    const win = page('grammatik', ['assets/data/grammatik.js', 'assets/data/grammatik_extra.js', 'assets/data/grammatik_furigana.js', 'assets/data/grammatik_plus.js']);
    chip(win, '7').dispatchEvent(new win.Event('click', { bubbles: true }));
    const g = win.document.querySelector('.group-empty[data-empty-for="7"]');
    expect(g.classList.contains('hidden')).toBe(false);
    expect(win.document.getElementById('empty').classList.contains('hidden')).toBe(true);
    // andere leere Lektion ist ausgeblendet
    expect(win.document.querySelector('.group-empty[data-empty-for="2"]').classList.contains('hidden')).toBe(true);
  });

  it('bei einer Suche verschwinden die Hinweise', () => {
    const win = page('grammatik', ['assets/data/grammatik.js', 'assets/data/grammatik_extra.js', 'assets/data/grammatik_furigana.js', 'assets/data/grammatik_plus.js']);
    search(win, 'たい');
    [...win.document.querySelectorAll('.group-empty')].forEach((g) => expect(g.classList.contains('hidden')).toBe(true));
  });
});
