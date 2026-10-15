"""Erzeugt assets/data/vokabular_tags.js (Tags für die Satz-Engine) — IDs werden aus dem
aktuellen Vokabular aufgelöst (erste Lektion, in der das Wort steht)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
from gen_vokabular import entries

GRUPPEN = [
 ('Personen / Subjekte', ['person', 'subj3'], 'おとこのひと おんなのひと こども おとこのこ おんなのこ'),
 ('Personen', ['person'], 'わたし あなた'),
 ('Familie & Freunde (Begleiter mit と)', ['person', 'family'], 'りょうしん ともだち かぞく'),
 ('Rollen/Berufe (Prädikatsnomen)', ['role'], 'せんせい かいしゃいん'),
 ('Essen', ['food'], 'すし てんぷら ラーメン ピザ ケーキ パン やさい くだもの さかな'),
 ('Getränke', ['drink'], 'みず コーヒー ビール ワイン コーラ ミルク'),
 ('Lesbares', ['readable'], 'ほん しんぶん まんが ざっし てがみ'),
 ('Dinge', ['thing'], 'かばん ペン カメラ とけい かさ スマホ'),
 ('Orte', ['place'], 'がっこう だいがく かいしゃ えき こうえん スーパー デパート としょかん びょういん レストラン ぎんこう'),
 ('Verkehrsmittel', ['transport'], 'でんしゃ バス じてんしゃ ちかてつ タクシー しんかんせん ひこうき'),
 ('い-Adjektive (Eigenschaft von Dingen)', ['i_adj'], 'おおきい ちいさい あたらしい やすい あかい あおい しろい くろい'),
 ('な-Adjektive (passend zu Orten)', ['na_adj', 'na_place'], 'しずか ゆうめい べんり'),
]

def main():
    first = {}
    for les, rows in entries().items():
        for v in rows:
            first.setdefault(v['kana'], (les, v))
    out = ['/* Semantische Tags für die Satz-Engine (window.VOKABULAR_TAGS).',
           '   Schlüssel = abgeleitete SRS-ID "v:<kana>|<lesson>" (siehe srs.js · srsId).',
           '   subj3 = 3. Person Singular mit Artikel (für korrekte deutsche Verbform „Der Mann isst …").',
           '   Erzeugt mit quellen/werkzeug/gen_tags.py — dort ändern, nicht hier. */',
           'window.VOKABULAR_TAGS = {']
    for title, tags, words in GRUPPEN:
        out.append('  /* ---- %s ---- */' % title)
        for w in words.split():
            if w not in first:
                raise SystemExit('nicht im Vokabular: ' + w)
            les, v = first[w]
            out.append('  "v:%s|%d": [%s],' % (w, les, ', '.join('"%s"' % t for t in tags)))
    out.append('};')
    open(os.path.join(ROOT, 'assets/data/vokabular_tags.js'), 'w').write('\n'.join(out) + '\n')
    print('ok')

if __name__ == '__main__':
    main()
