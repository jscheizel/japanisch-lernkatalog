"""Erzeugt assets/data/vokabular_beispiele.js: je Vokabel ein Beispielsatz.
Neue Sätze aus beispiele_neu.py haben Vorrang; sonst wird der Satz des alten Bestands
übernommen, wenn dort dasselbe Wort (Kana + Wortart + Schreibweise) stand."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
from gen_vokabular import entries
from beispiele_neu import N

def main():
    old = [json.loads(m) for m in re.findall(r'^\s*(\{"kanji".*\}),?\s*$', open(os.path.join(HERE, 'vokabular_alt.js')).read(), re.M)]
    ob = {}
    for m in re.finditer(r'^\s*"([^"|]+)\|(\d+)":\s*(\{.*\}),?\s*$', open(os.path.join(HERE, 'vokabular_beispiele_alt.js')).read(), re.M):
        ob[(m.group(1), int(m.group(2)))] = json.loads(m.group(3))
    out = ['/* Vokabular-Beispielsätze — je Wort ein natürlicher Beispielsatz plus kurze deutsche Verwendungsnotiz.',
           '   Additiv (wie grammatik_plus.js), greift nur, wenn vorhanden.',
           '   Schlüssel: "<kana>|<lektion>" → { jp, r (Romaji), de (Übersetzung), note (Nutzungshinweis) }.',
           '   Erzeugt mit quellen/werkzeug/gen_beispiele.py — dort ändern, nicht hier. */',
           'window.VOKABULAR_BEISPIELE = {']
    n = fehlt = 0
    for les, rows in entries().items():
        out.append('  /* Lektion %d */' % les)
        for v in rows:
            b = None
            if v['kana'] in N:
                jp, r, de, note = N[v['kana']]
                b = {'jp': jp, 'r': r, 'de': de, 'note': note}
            else:
                for o in old:
                    if o['kana'] == v['kana'] and o['pos'] == v['pos'] and (o['kanji'] == v['kanji'] or not o['kanji'] or not v['kanji']) and (o['kana'], o['lesson']) in ob:
                        b = ob[(o['kana'], o['lesson'])]; break
            if not b:
                fehlt += 1; print('ohne Beispiel:', v['kana']); continue
            out.append('  %s: %s,' % (json.dumps('%s|%d' % (v['kana'], les), ensure_ascii=False), json.dumps(b, ensure_ascii=False, separators=(',', ':'))))
            n += 1
    out.append('};')
    open(os.path.join(ROOT, 'assets/data/vokabular_beispiele.js'), 'w').write('\n'.join(out) + '\n')
    print(n, 'Beispiele,', fehlt, 'ohne')

if __name__ == '__main__':
    main()
