# Daten-Generatoren

- `vokabeln_l0.py`, `vokabeln_l1_13.py` — kuratierte Wortlisten je Lektion → `gen_vokabular.py`
- `grammatik_daten.py` — Grammatik inkl. Zusatzbeispielen und Übungen → `gen_grammatik.py`
  (schreibt auch die Furigana; Sonderfälle in `OVERRIDE`/`PRIO`/`fix()`)
- `gen_kanji.py` — Kanji je Lektion; Lesungen/Beispiele bekannter Kanji aus `kanji_alt.js`
- `gen_tags.py` — Tags für die Satz-Engine (`saetze.js` ist handgeschrieben)
- `beispiele_neu.py` + `gen_beispiele.py` — Beispielsatz je Vokabel (alter Bestand: `*_alt.js`)
- `themen.py` — Lektionsthemen und Datum; `romaji.py` — Kana → Rōmaji

Reihenfolge und Aufrufe: siehe `../BERICHT.md`.
