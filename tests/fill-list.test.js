// Füll-Listen: Lektionen wählen, in 10er-Runden Vokabeln selbst einschätzen (sicher/unsicher/nicht).
import { describe, it, expect, beforeEach } from 'vitest';
import { loadWithData } from './helpers/load.js';

function fakeStorage() {
  const d = {};
  return {
    getItem: (k) => (k in d ? d[k] : null),
    setItem: (k, v) => { d[k] = String(v); },
    removeItem: (k) => { delete d[k]; },
  };
}

let win, SRS;
beforeEach(() => {
  win = loadWithData(['assets/app.js', 'assets/srs.js'], {
    html: '<!DOCTYPE html><html><body data-page="listen"></body></html>',
  });
  SRS = win.SRS;
  SRS._useStorage(fakeStorage());
});

const vocabOf = (lessons) => win.VOKABULAR.filter((v) => lessons.includes(v.lesson)).map((v) => SRS.srsId('vocab', v));
// deterministischer Zufall
function seeded(seed) { let s = seed; return () => { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }

describe('Füll-Liste anlegen', () => {
  it('merkt sich die Lektionen (sortiert, ohne Dubletten) und startet leer', () => {
    const l = SRS.createFillList('Füll', [3, 1, 2, 1]);
    expect(l.fill.lessons).toEqual([1, 2, 3]);
    expect(l.items).toEqual([]);
    const info = SRS.fillInfo(l.id);
    expect(info.total).toBe(vocabOf([1, 2, 3]).length);
    expect(info.remaining).toBe(info.total);
    expect(info.started).toBe(false);
    expect(SRS.isFillList(l.id)).toBe(true);
  });

  it('ohne Lektionen wird keine Liste angelegt', () => {
    expect(SRS.createFillList('Leer', [])).toBeNull();
    expect(SRS.lists()).toHaveLength(0);
  });

  it('normale Listen sind keine Füll-Listen', () => {
    const l = SRS.createList('Normal');
    expect(SRS.isFillList(l.id)).toBe(false);
    expect(SRS.fillInfo(l.id)).toBeNull();
    expect(SRS.fillBatch(l.id)).toEqual([]);
    expect(SRS.fillRate(l.id, vocabOf([1])[0], 'no')).toBeNull();
  });
});

describe('Runden und Einschätzung', () => {
  it('fillBatch liefert 10 verschiedene Vokabeln aus den gewählten Lektionen', () => {
    const l = SRS.createFillList('F', [1, 2, 3]);
    const batch = SRS.fillBatch(l.id, undefined, seeded(7));
    expect(batch).toHaveLength(SRS.FILL_BATCH);
    expect(SRS.FILL_BATCH).toBe(10);
    expect(new Set(batch.map((b) => b.id)).size).toBe(10);
    batch.forEach((b) => expect([1, 2, 3]).toContain(b.data.lesson));
  });

  it('Beispiel aus dem Feature: 3 sicher, 3 unsicher, 4 nicht → 7 in der Liste', () => {
    const l = SRS.createFillList('F', [1, 2, 3]);
    const batch = SRS.fillBatch(l.id, 10, seeded(1));
    const ratings = ['sure', 'sure', 'sure', 'unsure', 'unsure', 'unsure', 'no', 'no', 'no', 'no'];
    batch.forEach((b, i) => SRS.fillRate(l.id, b.id, ratings[i]));
    const list = SRS.lists().find((x) => x.id === l.id);
    expect(list.items).toHaveLength(7);
    // Scores: sicher = beherrscht, unsicher = 40, nicht = 0
    batch.slice(0, 3).forEach((b) => { expect(SRS.scoreOf(b.id)).toBe(SRS.MASTER_AT); expect(list.items).not.toContain(b.id); });
    batch.slice(3, 6).forEach((b) => expect(SRS.scoreOf(b.id)).toBe(40));
    batch.slice(6).forEach((b) => expect(SRS.scoreOf(b.id)).toBe(0));
    const info = SRS.fillInfo(l.id);
    expect(info.done).toBe(10);
    expect(info.remaining).toBe(info.total - 10);
    expect(info.started).toBe(true);

    // Nächster Tag: 10 NEUE Vokabeln, keine schon gesehenen
    const seen = new Set(batch.map((b) => b.id));
    const next = SRS.fillBatch(l.id, 10, seeded(2));
    expect(next).toHaveLength(10);
    next.forEach((b) => expect(seen.has(b.id)).toBe(false));
    next.forEach((b, i) => SRS.fillRate(l.id, b.id, i < 8 ? 'sure' : 'no'));
    expect(SRS.lists().find((x) => x.id === l.id).items).toHaveLength(9);
  });

  it('sicher senkt einen höheren Score nicht; unsicher/nicht setzen ihn fest', () => {
    const l = SRS.createFillList('F', [1]);
    const [a, b] = vocabOf([1]);
    SRS.__test.setScore(a, 95);
    SRS.__test.setScore(b, 70);
    SRS.fillRate(l.id, a, 'sure');
    SRS.fillRate(l.id, b, 'unsure');
    expect(SRS.scoreOf(a)).toBe(95);
    expect(SRS.scoreOf(b)).toBe(40);
  });

  it('zählt nicht als Übung (kein Tagesgewinn, keine Reviews)', () => {
    const l = SRS.createFillList('F', [1]);
    const before = JSON.parse(SRS.exportJSON()).stats.totalReviews;
    SRS.fillRate(l.id, vocabOf([1])[0], 'sure');
    expect(SRS.dailyGain()).toBe(0);
    expect(JSON.parse(SRS.exportJSON()).stats.totalReviews).toBe(before);
  });

  it('unbekannte Bewertung wird ignoriert', () => {
    const l = SRS.createFillList('F', [1]);
    expect(SRS.fillRate(l.id, vocabOf([1])[0], 'vielleicht')).toBeNull();
    expect(SRS.fillInfo(l.id).done).toBe(0);
  });

  it('manuell hinzugefügte Vokabeln werden nicht mehr abgefragt', () => {
    const l = SRS.createFillList('F', [1]);
    const v = vocabOf([1])[0];
    SRS.addToList(l.id, [v]);
    expect(SRS.fillRemaining(l.id)).not.toContain(v);
  });

  it('wenn alles durchgegangen ist: remaining 0, leere Runde; letzte Runde kann kürzer sein', () => {
    const l = SRS.createFillList('F', [1]);
    const total = vocabOf([1]).length;
    let rounds = 0;
    for (;;) {
      const batch = SRS.fillBatch(l.id, 10, seeded(rounds + 3));
      if (!batch.length) break;
      expect(batch.length).toBe(Math.min(10, total - rounds * 10));
      batch.forEach((b) => SRS.fillRate(l.id, b.id, 'sure'));
      rounds++;
    }
    expect(rounds).toBe(Math.ceil(total / 10));
    expect(SRS.fillInfo(l.id).remaining).toBe(0);
  });
});

describe('Füll-Daten überstehen Export/Import und Merge', () => {
  it('Listen-Export enthält Lektionen + gesehene Vokabeln; Import stellt sie wieder her', () => {
    const l = SRS.createFillList('Teilen', [2]);
    const [a, b] = vocabOf([2]);
    SRS.fillRate(l.id, a, 'sure');
    SRS.fillRate(l.id, b, 'no');
    const json = SRS.exportListJSON(l.id);
    const parsed = JSON.parse(json);
    expect(parsed.fill).toEqual({ lessons: [2], seen: [a, b] });
    const res = SRS.importListJSON(json);
    expect(res.ok).toBe(true);
    expect(SRS.isFillList(res.list.id)).toBe(true);
    expect(SRS.fillInfo(res.list.id).done).toBe(2);
  });

  it('Komplett-Sicherung: Merge vereinigt gesehene Vokabeln', () => {
    const l = SRS.createFillList('F', [1]);
    const [a, b] = vocabOf([1]);
    SRS.fillRate(l.id, a, 'sure');
    const backup = SRS.exportJSON();
    SRS.fillRate(l.id, b, 'no');
    expect(SRS.importJSON(backup).ok).toBe(true);
    const list = SRS.lists().find((x) => x.id === l.id);
    expect(list.fill.seen.sort()).toEqual([a, b].sort());
    expect(list.items).toContain(b);
    expect(SRS.isFillList(l.id)).toBe(true);
  });
});
