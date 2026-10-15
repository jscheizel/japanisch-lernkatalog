"""Kana → Rōmaji (Hepburn mit Längenstrichen), passend zum Stil von vokabular.js."""
import re

_H = {
 'あ':'a','い':'i','う':'u','え':'e','お':'o','か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko',
 'さ':'sa','し':'shi','す':'su','せ':'se','そ':'so','た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to',
 'な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho',
 'ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','や':'ya','ゆ':'yu','よ':'yo',
 'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro','わ':'wa','を':'o','ん':'n',
 'が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go','ざ':'za','じ':'ji','ず':'zu','ぜ':'ze','ぞ':'zo',
 'だ':'da','ぢ':'ji','づ':'zu','で':'de','ど':'do','ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo',
 'ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ぁ':'a','ぃ':'i','ぅ':'u','ぇ':'e','ぉ':'o',
 'ゔ':'vu',
}
_Y = {'ゃ':'a','ゅ':'u','ょ':'o'}

def _kata2hira(s):
    return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)

def kana2romaji(kana, suru=False):
    s = _kata2hira(kana.replace('～', '~'))
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        nx = s[i + 1] if i + 1 < len(s) else ''
        if c == 'っ':
            nr = _H.get(nx, '')
            if nr:
                out.append('t' if nr.startswith('ch') else nr[0])
            i += 1; continue
        if c == 'ー':
            if out:
                out[-1] = out[-1][:-1] + {'a':'ā','i':'ī','u':'ū','e':'ē','o':'ō'}.get(out[-1][-1], out[-1][-1])
            i += 1; continue
        if nx in _Y and c in _H:
            base = _H[c]
            if base in ('shi', 'chi', 'ji'):
                out.append(base[:-1] + _Y[nx])
            else:
                out.append(base[:-1] + 'y' + _Y[nx])
            i += 2; continue
        if c in ('ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ') and out:
            # Katakana-Fremdwörter: ティ→ti, フィ→fi, ウェ→we, シェ→she, ジェ→je, チェ→che
            prev = out.pop()
            v = _H[c]
            if prev in ('te', 'de'):
                out.append(prev[0] + v)
            elif prev == 'fu':
                out.append('f' + v)
            elif prev == 'u':
                out.append('w' + v)
            elif prev in ('shi', 'ji', 'chi'):
                out.append(prev[:-1] + v)
            else:
                out.append(prev + v)
            i += 1; continue
        if c == 'ん' and nx and _H.get(nx, ' ')[0] in 'aiueoy':
            out.append("n'"); i += 1; continue
        out.append(_H.get(c, c))
        i += 1
    r = ''.join(out).replace("n'", 'n')
    # Längen: ou/oo → ō, uu → ū, aa → ā, ee → ē (ii bleibt wie im Bestand)
    r = r.replace('ou', 'ō').replace('oo', 'ō').replace('uu', 'ū').replace('aa', 'ā').replace('ee', 'ē')
    # „wa"-Partikel ist hier nicht relevant; します-Verben getrennt schreiben
    if suru and r.endswith('shimasu') and len(r) > 7:
        r = r[:-7].rstrip() + ' shimasu'
    return r

if __name__ == '__main__':
    for w in ['べんきょうします','コーヒー','しんかんせん','ちょっと','シャワー','パーティー','ウェイター','きっぷ','おおきい','とうきょう','ジョギング','コインランドリー','かします','はなします','さんぽします','フィンランド']:
        print(w, kana2romaji(w, w.endswith('します') and w not in ('かします','はなします')))
