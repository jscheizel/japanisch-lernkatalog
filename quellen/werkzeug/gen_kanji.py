"""Erzeugt assets/data/kanji.js: Kanji je Lektion (level = "L<n>").
Bestehende Einträge (Lesungen, Strichzahl, Beispiele) werden aus dem alten Katalog übernommen,
die neuen stammen aus dem Kanji-Buch der Unterrichts-PDFs (Genki Kanji, Bedeutungen übersetzt).
Aufruf: python3 -I quellen/werkzeug/gen_kanji.py <alter-kanji.js>"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

LEKTION = [
 (0, '', '一二三四五六七八九十日月火水木金土山川田口門人子女先生学私車円'),
 (2, 'Genki 第3課', '百千万年'),
 (5, 'Genki 第4課', '上下中大小本半分力何'),
 (7, 'Genki 第5課', '明休体好男林森間畑岩石'),
 (10, 'Genki 第6課', '目耳手足雨竹米貝糸'),
 (12, 'Genki 第7課', '花茶肉文字物牛馬鳥魚'),
]

def ex(*t):
    return [{'w': w, 'r': r, 'm': m} for w, r, m in t]

NEU = {
 '門': dict(on=['モン'], kun=['かど'], meaning='Tor', strokes=8, examples=ex(('門','もん','Tor'),('ブランデンブルグ門','ブランデンブルグもん','Brandenburger Tor'),('専門','せんもん','Fachgebiet'))),
 '体': dict(on=['タイ'], kun=['からだ'], meaning='Körper', strokes=7, examples=ex(('体','からだ','Körper'),('大きい体','おおきいからだ','großer Körper'),('体力','たいりょく','Körperkraft'))),
 '林': dict(on=['リン'], kun=['はやし'], meaning='Wäldchen, Hain', strokes=8, examples=ex(('林','はやし','Wäldchen; Hayashi (Name)'),('林さん','はやしさん','Herr/Frau Hayashi'),('小林','こばやし','Kobayashi (Name)'))),
 '森': dict(on=['シン'], kun=['もり'], meaning='Wald', strokes=12, examples=ex(('森','もり','Wald'),('森の中','もりのなか','im Wald'),('森林','しんりん','Wälder'))),
 '畑': dict(on=[], kun=['はたけ','はた'], meaning='Acker, Feld', strokes=9, examples=ex(('畑','はたけ','Acker'),('田畑','たはた','Reis- und Ackerfelder'),('花畑','はなばたけ','Blumenfeld'))),
 '岩': dict(on=['ガン'], kun=['いわ'], meaning='Felsen', strokes=8, examples=ex(('岩','いわ','Felsen'),('大きい岩','おおきいいわ','großer Felsen'),('岩田','いわた','Iwata (Name)'))),
 '目': dict(on=['モク'], kun=['め'], meaning='Auge', strokes=5, examples=ex(('目','め','Auge'),('大きい目','おおきいめ','große Augen'),('目次','もくじ','Inhaltsverzeichnis'))),
 '耳': dict(on=['ジ'], kun=['みみ'], meaning='Ohr', strokes=6, examples=ex(('耳','みみ','Ohr'),('馬の耳','うまのみみ','Ohr des Pferdes'),('耳鼻科','じびか','HNO-Heilkunde'))),
 '竹': dict(on=['チク'], kun=['たけ'], meaning='Bambus', strokes=6, examples=ex(('竹','たけ','Bambus'),('竹の子','たけのこ','Bambussprosse'),('竹田','たけだ','Takeda (Name)'))),
 '米': dict(on=['マイ','ベイ'], kun=['こめ'], meaning='Reis; Amerika', strokes=6, examples=ex(('米','こめ','Reis'),('米国','べいこく','USA'),('新米','しんまい','neuer Reis; Neuling'))),
 '貝': dict(on=[], kun=['かい'], meaning='Muschel', strokes=7, examples=ex(('貝','かい','Muschel'),('貝がら','かいがら','Muschelschale'),('貝が好き','かいがすき','Muscheln mögen'))),
 '糸': dict(on=['シ'], kun=['いと'], meaning='Faden', strokes=6, examples=ex(('糸','いと','Faden'),('毛糸','けいと','Wolle'),('糸電話','いとでんわ','Dosentelefon'))),
 '茶': dict(on=['チャ','サ'], kun=[], meaning='Tee', strokes=9, examples=ex(('お茶','おちゃ','Tee'),('抹茶','まっちゃ','Matcha'),('紅茶','こうちゃ','schwarzer Tee'),('喫茶店','きっさてん','Café'))),
 '肉': dict(on=['ニク'], kun=[], meaning='Fleisch', strokes=6, examples=ex(('肉','にく','Fleisch'),('牛肉','ぎゅうにく','Rindfleisch'),('鳥肉','とりにく','Hühnerfleisch'))),
 '字': dict(on=['ジ'], kun=[], meaning='Schriftzeichen, Buchstabe', strokes=6, examples=ex(('漢字','かんじ','Kanji'),('文字','もじ','Schriftzeichen'),('絵文字','えもじ','Emoji'),('数字','すうじ','Ziffer, Zahl'))),
 '物': dict(on=['ブツ','モツ'], kun=['もの'], meaning='Ding, Sache', strokes=8, examples=ex(('物','もの','Ding'),('食べ物','たべもの','Essen'),('買い物','かいもの','Einkauf'),('着物','きもの','Kimono'),('荷物','にもつ','Gepäck'))),
 '牛': dict(on=['ギュウ'], kun=['うし'], meaning='Rind, Kuh', strokes=4, examples=ex(('牛','うし','Rind'),('牛肉','ぎゅうにく','Rindfleisch'),('牛乳','ぎゅうにゅう','Milch'))),
 '馬': dict(on=['バ'], kun=['うま'], meaning='Pferd', strokes=10, examples=ex(('馬','うま','Pferd'),('馬力','ばりき','Pferdestärke'),('馬車','ばしゃ','Kutsche'))),
 '鳥': dict(on=['チョウ'], kun=['とり'], meaning='Vogel', strokes=11, examples=ex(('鳥','とり','Vogel'),('焼き鳥','やきとり','Yakitori'),('白鳥','はくちょう','Schwan'))),
 '魚': dict(on=['ギョ'], kun=['さかな'], meaning='Fisch', strokes=11, examples=ex(('魚','さかな','Fisch'),('金魚','きんぎょ','Goldfisch'),('魚屋','さかなや','Fischladen'))),
}

def load_old(path):
    s = open(path).read()
    rows = {}
    for m in re.finditer(r'^\s*(\{"k":.*\}),?\s*$', s, re.M):
        o = json.loads(m.group(1))
        rows[o['k']] = o
    return rows

def main(old_path):
    old = load_old(old_path)
    lines = ['/* Kanji — je Lektion des Japanischkurses (level = "L<n>", L0 = vorausgesetzt).',
             '   Felder: k (Kanji), on (On-Lesung, Katakana), kun (Kun-Lesung, Hiragana; "-" trennt Okurigana),',
             '   meaning (Bedeutung), strokes (Strichzahl), level, cls (Quelle im Kanji-Buch), examples [{w,r,m}].',
             '   音 = On-Lesung (sinojapanisch) · 訓 = Kun-Lesung (japanisch).',
             '   Erzeugt mit quellen/werkzeug/gen_kanji.py — dort ändern, nicht hier. */',
             'window.KANJI = [']
    n = 0
    for les, cls, chars in LEKTION:
        lines.append('  /* ===== L%d ===== */' % les)
        for c in chars:
            if c in NEU:
                d = dict(k=c, **NEU[c])
            elif c in old:
                o = old[c]
                d = {k: o[k] for k in ('k', 'on', 'kun', 'meaning', 'strokes', 'examples')}
            else:
                raise SystemExit('Kanji ohne Daten: ' + c)
            row = {'k': d['k'], 'on': d['on'], 'kun': d['kun'], 'meaning': d['meaning'], 'strokes': d['strokes'],
                   'level': 'L%d' % les, 'cls': cls, 'examples': d['examples']}
            lines.append('  ' + json.dumps(row, ensure_ascii=False, separators=(',', ':')) + ',')
            n += 1
    lines.append('];')
    open(os.path.join(ROOT, 'assets/data/kanji.js'), 'w').write('\n'.join(lines) + '\n')
    print(n, 'Kanji')

if __name__ == '__main__':
    main(sys.argv[1])
