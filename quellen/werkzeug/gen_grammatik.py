"""Erzeugt grammatik.js, grammatik_extra.js, grammatik_plus.js und grammatik_furigana.js.
Aufruf: python3 -I quellen/werkzeug/gen_grammatik.py"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
from grammatik_daten import G
from furigana import Furi
from gen_vokabular import entries
from gen_kanji import LEKTION, NEU, load_old

# Lesungen, die das Wörterbuch nicht eindeutig trifft (Satz → annotierter Satz)
OVERRIDE = {}
# Einzelwörter mit Vorrang (Zahl+Zähler usw.)
PRIO = [('七じ', 'しちじ'), ('四じ', 'よじ'), ('九じ', 'くじ'), ('一人', 'ひとり'), ('二人', 'ふたり'), ('明日', 'あした'),
        ('今', 'いま'), ('何', 'なに'), ('何です', 'なんです'), ('何ですか', 'なんですか'), ('日本', 'にほん'), ('上', 'うえ'), ('下', 'した'),
        ('中', 'なか'), ('人', 'ひと'), ('日', 'ひ'), ('月よう日', 'げつようび'), ('土よう日', 'どようび'), ('行きます', 'いきます'),
        ('大きい', 'おおきい'), ('高い', 'たかい'), ('私', 'わたし'), ('子ども', 'こども'), ('学生', 'がくせい'), ('先生', 'せんせい'),
        ('赤い', 'あかい'), ('青い', 'あおい'), ('山', 'やま'), ('川', 'かわ'), ('木', 'き'), ('水', 'みず'), ('車', 'くるま'), ('犬', 'いぬ'),
        ('間', 'あいだ'), ('時', 'とき'), ('休みます', 'やすみます'), ('朝', 'あさ'), ('見ます', 'みます'), ('一', 'ひと'), ('大阪', 'おおさか'),
        ('父', 'ちち'), ('四時', 'よじ'), ('人', 'ひと')]

def furi_engine():
    f = Furi()
    for w, r in PRIO:
        f.add(w, r, prio=True)
    for rows in entries().values():
        for v in rows:
            if v['kanji']:
                f.add(v['kanji'], v['kana'])
    old = load_old(os.path.join(HERE, 'kanji_alt.js'))
    for _, _, chars in LEKTION:
        for c in chars:
            exs = NEU[c]['examples'] if c in NEU else old[c]['examples']
            for e in exs:
                f.add(e['w'], e['r'])
    return f

def fix(a):
    a = a.replace('まい{日|び}', 'まい{日|にち}')
    a = re.sub(r'([ァ-ヶー])\{人\|ひと\}', r'\1{人|じん}', a)
    return a

def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))

def main():
    head = '/* %s — Japanischkurs (Unterrichts-PDFs), Lektion 0–13.\n   Erzeugt mit quellen/werkzeug/gen_grammatik.py — dort ändern, nicht hier.\n'
    # grammatik.js
    L = [head % 'Grammatik' + '   Felder: lesson, pattern (Muster), title, bildung, erklaerung, beispiele [{jp, r (Rōmaji), de}]. */', 'window.GRAMMATIK = [']
    cur = None
    for g in G:
        if g['lesson'] != cur:
            cur = g['lesson']; L.append('  /* ===== Lektion %d ===== */' % cur)
        L.append('  ' + js({k: g[k] for k in ('lesson', 'pattern', 'title', 'bildung', 'erklaerung', 'beispiele')}) + ',')
    L.append('];')
    open(os.path.join(ROOT, 'assets/data/grammatik.js'), 'w').write('\n'.join(L) + '\n')
    # grammatik_extra.js
    E = [head % 'Zusätzliche Beispielsätze je Grammatikpunkt' + '   Schlüssel = exakter `pattern`-String aus grammatik.js; werden im Katalog an die\n   vorhandenen Beispiele angehängt. */', 'window.GRAMMATIK_EXTRA = {']
    for g in G:
        if g['extra']:
            E.append('  %s: [' % js(g['pattern']))
            E.append(',\n'.join('    ' + js(b) for b in g['extra']))
            E.append('  ],')
    E.append('};')
    open(os.path.join(ROOT, 'assets/data/grammatik_extra.js'), 'w').write('\n'.join(E) + '\n')
    # grammatik_plus.js
    P = [head % 'Erweiterte Grammatik (window.GRAMMATIK_PLUS)' + '''   Schlüssel = exakter `pattern`-String aus grammatik.js.
   Felder je Eintrag (alle optional):
     erklaerung_lang : ausführliche Erklärung mit Nuancen
     fehler          : Liste häufiger Fehler
     kontrast        : Liste {a, b, note} — Abgrenzung verwandter Formen
     uebungen        : Liste von Übungen
                       { typ:"mc",    frage, optionen:[…], richtig:Index, erkl }
                       { typ:"cloze", satz (mit ＿), luecke:"…", erkl }
   Wird im Katalog additiv unter „Mehr erklären" angezeigt; Übungen laufen im Trainer mit. */''', 'window.GRAMMATIK_PLUS = {']
    for g in G:
        P.append('  %s: %s,' % (js(g['pattern']), json.dumps(g['plus'], ensure_ascii=False, indent=2).replace('\n', '\n  ')))
    P.append('};')
    open(os.path.join(ROOT, 'assets/data/grammatik_plus.js'), 'w').write('\n'.join(P) + '\n')
    # grammatik_furigana.js
    f = furi_engine()
    F = [head % 'Furigana zu den Grammatik-Beispielsätzen (window.GRAMMATIK_FURIGANA)' + '   Schlüssel = exakter `jp`-String aus grammatik.js / grammatik_extra.js.\n   Notation: {Basis|Lesung} = Ruby-Annotation über Kanji; alles andere ist Klartext. */', 'window.GRAMMATIK_FURIGANA = {']
    seen, unknown = set(), []
    for g in G:
        for b in g['beispiele'] + g['extra']:
            jp = b['jp']
            if jp in seen: continue
            seen.add(jp)
            a = OVERRIDE.get(jp) or fix(f.annotate(jp))
            if '|?}' in a: unknown.append(a)
            F.append('  %s: %s,' % (js(jp), js(a)))
    F.append('};')
    open(os.path.join(ROOT, 'assets/data/grammatik_furigana.js'), 'w').write('\n'.join(F) + '\n')
    print(len(G), 'Grammatikpunkte;', len(seen), 'Sätze;', 'unbekannt:', unknown)

if __name__ == '__main__':
    main()
