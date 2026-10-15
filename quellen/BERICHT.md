# Migration: Minna no Nihongo → Unterrichts-PDFs

Die App-Inhalte (`assets/data/*.js`, Kanji-SVGs) stammen jetzt aus den 13 Unterrichts-PDFs in
diesem Ordner. Jedes PDF ist eine Lektion (nach Datum), **Lektion 0** ist der vorausgesetzte Stoff:
alles, was in den PDFs als „Wiederholung" geübt oder ohne Einführung benutzt wird.

## Umfang je Lektion

| L | Datum | Thema | Vokabeln | Grammatik | Kanji |
|---|---|---|---|---|---|
| 0 | – | Grundwortschatz (vorausgesetzt) | 243 | 21 | 31 |
| 1 | 24.06. | ～たい / ～がほしい | 23 | 3 | – |
| 2 | 15.07. | Neue Verben | 33 | – | 4 (百千万年) |
| 3 | 22.07. | て-Form & ～てください | 16 | 5 | – |
| 4 | 29.07. | ～ましょうか | 8 | 1 | – |
| 5 | 05.08. | ～ています (gerade / regelmäßig) | 36 | 2 | 10 (上下中大小本半分力何) |
| 6 | 12.08. | ～ています (Zustand), kennen | 37 | 4 | – |
| 7 | 19.08. | Wiederholung & Kanji | 32 | – | 11 (明休体好男林森間畑岩石) |
| 8 | 26.08. | V-て、V-て (Handlungsfolge) | 21 | 1 | – |
| 9 | 16.09. | Adjektive: Vergangenheit & Verneinung | 40 | 3 | – |
| 10 | 23.09. | Adjektive verbinden (～くて / ～で) | 24 | 2 | 9 (目耳手足雨竹米貝糸) |
| 11 | 30.09. | dürfen / nicht dürfen | 16 | 2 | – |
| 12 | 07.10. | Wiederholung & Kanji | 27 | 1 | 10 (花茶肉文字物牛馬鳥魚) |
| 13 | 14.10. | ない-Form & ～ないでください | 21 | 2 | – |
| | | **Summe** | **577** | **47** | **75** |

## Entscheidungen und unsichere Stellen (bitte kurz prüfen)

- **Japanische Wörter zu deutschen Listen.** Die Vokabellisten in den PDFs sind meist nur deutsch
  (zum Ausfüllen). Die japanischen Wörter stammen aus Wortbanken, Übungen und euren handschriftlichen
  Lösungen; wo nichts davon passte, habe ich das übliche Wort gewählt (z. B. „Wohnzimmer" → リビング,
  „Kollege" → どうりょう, „Bank" → ぎんこう).
- **Kanji 上下中大小本半分力何** kommen schon ab dem ersten PDF in Lesesätzen vor, werden aber erst
  am 05.08. im Kanji-Buch (第4課) eingeführt → **Lektion 5**. Genauso 石 (erst Zusatz am 19.08.,
  dann im 第6課) → Lektion 7.
- **Lektion 1** enthält neben ～たい/～ほしい die Wörter, die zuerst in den neuen Übungen dieser Stunde
  auftauchen (Kino, Klavier, Geschenk, Handy …); die übrigen Wörter des ersten PDFs sind Wiederholung → L0.
- **Doppelte „New"-Wörter** (z. B. けっこんします, ごみをすてます) stehen nur in der Lektion, in der sie
  zuerst vorkommen.
- **Verben ohne Objekt.** Wie bisher steht ein Verb einzeln; das typische Objekt steht im Deutschen
  (z. B. みがきます „putzen (歯を～ = Zähne putzen)").
- **Grammatik-Erklärungen** sind in den PDFs fast nur Tabellen und Übungen. Erklärungen, häufige
  Fehler und Zusatzübungen habe ich selbst geschrieben; die Beispielsätze sind an die PDF-Sätze angelehnt.
- **Beispielsätze je Vokabel:** 397 aus dem alten Bestand übernommen (gleiches Wort), 180 neu geschrieben.
- **Wörterbuchform und た-Form** kommen im Kurs noch nicht vor. Im Verbformen-Trainer sind sie daher
  gesperrt, bis der ganze Lernpfad freigeschaltet ist („Alle freischalten" öffnet sie).
- **Lernstand** wurde zurückgesetzt (neuer Speicher-Schlüssel `katalog_srs_v2`); der alte Stand bleibt
  unberührt im Browser liegen.

## Neu erzeugen

Die Datendateien sind generiert — Änderungen bitte in `quellen/werkzeug/` machen und neu erzeugen:

```bash
python3 -I quellen/werkzeug/gen_vokabular.py
python3 -I quellen/werkzeug/gen_kanji.py quellen/werkzeug/kanji_alt.js
python3 -I quellen/werkzeug/gen_grammatik.py
python3 -I quellen/werkzeug/gen_tags.py
python3 -I quellen/werkzeug/gen_beispiele.py
```

`quellen/extrakt/L*.json` ist die Rohauswertung je PDF (Abschnitte, Wörter, Kanji, Grammatik).
