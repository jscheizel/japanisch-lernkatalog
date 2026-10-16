"""Erzeugt assets/data/vokabular.js aus den kuratierten Listen.
Aufruf (aus dem Repo-Wurzelverzeichnis): python3 -I quellen/werkzeug/gen_vokabular.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from romaji import kana2romaji
from vokabeln_l0 import L0
from vokabeln_l1_13 import L
from themen import THEMEN, DATUM

ROOT = os.path.dirname(os.path.dirname(HERE))

# Eigennamen (Orte, Sehenswürdigkeiten, Feiertage) muss man nur lesen können → kein Vokabular.
# Länder bleiben (sie stecken in ～人／～語 und vielen Übungen).
EIGENNAMEN = set('''とうきょう おおさか きょうと ベルリン ミュンヘン あさくさ しんじゅく しぶや ほっかいどう ちば
ローマ ロンドン パリ よこはま おきなわ ひろしま はこね ふじさん スカイツリー アジア
クリスマス イースター クリスマスマーケット クリスマスツリー'''.split())
# Wörter, die nur in Lesetexten der Stunden vorkommen: vermutlich schon früher gelernt → Lektion 0.
LESETEXT_NACH_L0 = set('''やきそば レシピ ソース えび すてき たのしい よる りょかん おさけ ふとん たたみ
いざかや いちば おみやげ かぶき ホットワイン キャンドル クレープ ホットチョコレート'''.split())

def entries():
    l1_kana = {k for _, k, _, _ in L[1]}
    later = [e for les in sorted(L) for e in L[les] if e[1] in LESETEXT_NACH_L0]
    lessons = {0: [e for e in L0 if e[1] not in l1_kana] + later}
    for les in sorted(L):
        lessons[les] = [e for e in L[les] if e[1] not in LESETEXT_NACH_L0]
    lessons = {k: [e for e in v if e[1] not in EIGENNAMEN] for k, v in lessons.items()}
    seen = []  # (kana, pos, kanji)
    out = {}
    for les in sorted(lessons):
        rows = []
        for kanji, kana, de, pos in lessons[les]:
            dup = any(k == kana and p == pos and (kj == kanji or not kj or not kanji) for k, p, kj in seen)
            if dup:
                continue
            if any(r['kana'] == kana for r in rows):
                raise SystemExit('ID-Kollision v:%s|%d' % (kana, les))
            seen.append((kana, pos, kanji))
            kj = '' if kanji == kana else kanji
            rows.append({'kanji': kj, 'kana': kana, 'romaji': kana2romaji(kana, pos == 'V. III' and kana.endswith('します') and kana != 'します'),
                         'de': de, 'pos': pos, 'lesson': les})
        out[les] = rows
    return out

def main():
    data = entries()
    lines = ['/* Vokabular — Japanischkurs (Unterrichts-PDFs 24.06.–14.10.2026), Lektion 0–13.',
             '   Lektion 0 = vorausgesetzter Wortschatz; ab Lektion 1 je Unterrichtsstunde (PDF) eine Lektion.',
             '   Felder: kanji (Schreibweise, "" = nur Kana), kana (Lesung), romaji, de (Bedeutung), pos (Wortart), lesson.',
             '   Verben in der ます-Form; Gruppe in pos (V. I = 五段, V. II = 一段, V. III = unregelmäßig).',
             '   Erzeugt mit quellen/werkzeug/gen_vokabular.py — dort ändern, nicht hier. */',
             'window.VOKABULAR = [']
    n = 0
    for les, rows in data.items():
        head = 'Lektion %d — %s' % (les, THEMEN[les]) + (' (%s)' % DATUM[les] if les in DATUM else '')
        lines.append('  /* ===== %s ===== */' % head)
        for r in rows:
            lines.append('  ' + json.dumps(r, ensure_ascii=False, separators=(',', ':')) + ',')
            n += 1
    lines.append('];')
    open(os.path.join(ROOT, 'assets/data/vokabular.js'), 'w').write('\n'.join(lines) + '\n')
    print(n, {k: len(v) for k, v in data.items()})

if __name__ == '__main__':
    main()
