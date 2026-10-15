// Integrität der Sidecar-Daten: alle Schlüssel verweisen auf echte Katalog-Einträge.
import { describe, it, expect, beforeAll } from 'vitest';
import { existsSync } from 'node:fs';
import { loadWithData, repoPath } from './helpers/load.js';

let win, patterns, vocabIds;
beforeAll(() => {
  win = loadWithData([
    'assets/data/vokabular_tags.js',
    'assets/data/saetze.js',
    'assets/data/grammatik_plus.js',
  ]);
  patterns = new Set((win.GRAMMATIK || []).map((g) => g.pattern));
  vocabIds = new Set((win.VOKABULAR || []).map((v) => 'v:' + v.kana + '|' + v.lesson));
});

describe('SATZ_TEMPLATES', () => {
  it('jeder Schlüssel ist ein existierendes Grammatik-Muster', () => {
    const bad = Object.keys(win.SATZ_TEMPLATES).filter((p) => !patterns.has(p));
    expect(bad).toEqual([]);
  });
  it('jede Vorlage hat jp, de, slots und (falls particle) eine blank', () => {
    const bad = [];
    Object.entries(win.SATZ_TEMPLATES).forEach(([p, arr]) => {
      arr.forEach((t, i) => {
        if (!t.jp || !t.de || !t.slots) bad.push(`${p}[${i}]`);
      });
    });
    expect(bad).toEqual([]);
  });
});

describe('GRAMMATIK_PLUS', () => {
  it('jeder Schlüssel ist ein existierendes Grammatik-Muster', () => {
    const bad = Object.keys(win.GRAMMATIK_PLUS).filter((p) => !patterns.has(p));
    expect(bad).toEqual([]);
  });
  it('Übungen haben einen gültigen Typ und eine Lösung', () => {
    const bad = [];
    Object.entries(win.GRAMMATIK_PLUS).forEach(([p, obj]) => {
      (obj.uebungen || []).forEach((ex, i) => {
        if (ex.typ === 'mc' && (!Array.isArray(ex.optionen) || typeof ex.richtig !== 'number')) bad.push(`${p}[${i}] mc`);
        if (ex.typ === 'cloze' && (ex.luecke == null || !ex.satz)) bad.push(`${p}[${i}] cloze`);
        if (['mc', 'cloze'].indexOf(ex.typ) === -1) bad.push(`${p}[${i}] typ?`);
      });
    });
    expect(bad).toEqual([]);
  });
});

describe('VOKABULAR_TAGS', () => {
  it('jeder Schlüssel löst auf eine echte Vokabel auf', () => {
    const bad = Object.keys(win.VOKABULAR_TAGS).filter((id) => !vocabIds.has(id));
    expect(bad).toEqual([]);
  });
});

describe('Kursinhalt: Lektionen 0–13 aus den Unterrichts-PDFs', () => {
  let kw;
  beforeAll(() => { kw = loadWithData(['assets/data/vokabular.js', 'assets/data/kanji.js', 'assets/data/grammatik.js']); });

  it('jede Lektion 0–13 hat Vokabeln — und es gibt keine anderen Lektionen', () => {
    const lessons = new Set(kw.VOKABULAR.map((v) => v.lesson));
    for (let L = 0; L <= 13; L++) expect(lessons.has(L), 'Lektion ' + L).toBe(true);
    expect([...lessons].every((L) => L >= 0 && L <= 13)).toBe(true);
  });

  it('keine ID-Kollision (v:kana|lesson ist eindeutig)', () => {
    const ids = kw.VOKABULAR.map((v) => v.kana + '|' + v.lesson);
    expect(ids.length).toBe(new Set(ids).size);
  });

  it('jede Vokabel hat alle Felder; Verben stehen in der ます-Form', () => {
    kw.VOKABULAR.forEach((v) => {
      ['kanji', 'kana', 'romaji', 'de', 'pos', 'lesson'].forEach((f) => expect(v, v.kana + '.' + f).toHaveProperty(f));
      expect(v.de.length, v.kana).toBeGreaterThan(0);
      if (/^V\./.test(v.pos)) expect(v.kana, v.kana).toMatch(/ます$/);
    });
  });

  it('Kanji sind nach Lektion gruppiert (level = "L<n>") und kommen je einmal vor', () => {
    const K = kw.KANJI;
    K.forEach((k) => expect(k.level, k.k).toMatch(/^L(\d|1[0-3])$/));
    expect(K.length).toBe(new Set(K.map((k) => k.k)).size);
  });

  it('die neuen Kanji der Kanji-Buch-Lektionen stehen in der richtigen Kurslektion', () => {
    const lv = (c) => (kw.KANJI.find((k) => k.k === c) || {}).level;
    [...'百千万年'].forEach((c) => expect(lv(c), c).toBe('L2'));
    [...'上下中大小本半分力何'].forEach((c) => expect(lv(c), c).toBe('L5'));
    [...'明休体好男林森間畑岩石'].forEach((c) => expect(lv(c), c).toBe('L7'));
    [...'目耳手足雨竹米貝糸'].forEach((c) => expect(lv(c), c).toBe('L10'));
    [...'花茶肉文字物牛馬鳥魚'].forEach((c) => expect(lv(c), c).toBe('L12'));
    [...'一二三十日月火水木金土山川田口門人子女先生学私車円'].forEach((c) => expect(lv(c), c).toBe('L0'));
  });

  it('jedes Kanji hat Lesungen, Strichzahl, Beispiele (w/r/m) und eine Strichreihenfolge-Datei', () => {
    kw.KANJI.forEach((k) => {
      expect(k.on.length + k.kun.length, k.k).toBeGreaterThan(0);
      expect(k.strokes, k.k).toBeGreaterThan(0);
      expect(k.examples.length, k.k).toBeGreaterThanOrEqual(2);
      k.examples.forEach((e) => ['w', 'r', 'm'].forEach((f) => expect(e[f], k.k + '.' + f).toBeTruthy()));
      const file = 'assets/kanjivg/' + k.k.codePointAt(0).toString(16).padStart(5, '0') + '.svg';
      expect(existsSync(repoPath(file)), file).toBe(true);
    });
  });

  it('Grammatik der Unterrichtsstunden steht in der richtigen Lektion', () => {
    const les = (p) => (kw.GRAMMATIK.find((g) => g.pattern === p) || {}).lesson;
    expect(les('V たいです')).toBe(1);
    expect(les('N が ほしいです')).toBe(1);
    expect(les('V て-Form')).toBe(3);
    expect(les('V-ましょうか')).toBe(4);
    expect(les('V-て も いいです')).toBe(11);
    expect(les('V ない-Form')).toBe(13);
    expect(les('V-ないで ください')).toBe(13);
  });
});

describe('Kanji 力 „Kraft, Stärke"', () => {
  let K;
  beforeAll(() => { K = (loadWithData(['assets/data/kanji.js']).KANJI) || []; });

  it('steht genau einmal im Katalog, mit zwei Strichen', () => {
    const hits = K.filter((k) => k.k === '力');
    expect(hits).toHaveLength(1);
    expect(hits[0].strokes).toBe(2);
    expect(hits[0].meaning).toContain('Kraft');
  });

  it('ist von 九 unterscheidbar: eigenes Zeichen, eigene Lesungen, eigene Bedeutung', () => {
    // Die beiden sehen sich zum Verwechseln ähnlich — sie dürfen sich in der Übung nicht
    // gegenseitig als Lösung durchgehen: keine gemeinsame Lesung, keine gemeinsame Bedeutung.
    const chikara = K.find((k) => k.k === '力'), kyuu = K.find((k) => k.k === '九');
    expect(kyuu).toBeTruthy();
    const shared = [].concat(chikara.on, chikara.kun).filter((r) => [].concat(kyuu.on, kyuu.kun).indexOf(r) !== -1);
    expect(shared).toEqual([]);
    expect(chikara.meaning).not.toBe(kyuu.meaning);
  });

  it('seine Beispielwörter haben w/r/m', () => {
    const k = K.find((x) => x.k === '力');
    k.examples.forEach((e, i) => ['w', 'r', 'm'].forEach((f) => expect(e[f], 'examples[' + i + '].' + f).toBeTruthy()));
  });
});

describe('„Zähne putzen" (L5)', () => {
  const find = (kana, lesson) => (win.VOKABULAR || []).filter((v) => v.kana === kana && v.lesson === lesson);

  it('folgt der Hausregel: Verb + Objekt-Hinweis im de-Feld', () => {
    const v = find('みがきます', 5)[0];
    expect(v.pos).toBe('V. I');
    expect(v.de).toContain('歯を～');
  });

  it('„Zähne" findet das Verb — der Begriff steht im de-Feld, nicht nur im Beispielsatz', () => {
    expect(find('みがきます', 5)[0].de.toLowerCase()).toContain('zähne');
  });

  it('歯 „der Zahn" steht genau einmal im Vokabular', () => {
    const ha = (win.VOKABULAR || []).filter((v) => v.kana === 'は' && v.de.indexOf('Zahn') !== -1);
    expect(ha).toHaveLength(1);
  });
});
