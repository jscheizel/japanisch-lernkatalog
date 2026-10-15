"""Einfache Furigana-Annotation ({Kanji|Lesung}) über ein Wörterbuch aus Vokabular + Kanji-Beispielen.
Längste passende Kanji-Folge gewinnt; Sonderfälle stehen in OVERRIDE (ganzer Satz)."""
import re

def is_kanji(c):
    return '一' <= c <= '鿿' or c in '々'

def align(word, reading):
    """Zerlegt word (Kanji+Kana) mit reading in [(kanji_run, lesung) | (kana, None)] oder None."""
    parts = re.findall(r'[一-鿿々]+|[^一-鿿々]+', word)
    pat = ''.join('(.+?)' if is_kanji(p[0]) else re.escape(kata2hira(p)) for p in parts)
    m = re.fullmatch(pat, kata2hira(reading))
    if not m:
        return None
    out, gi = [], 1
    for p in parts:
        if is_kanji(p[0]):
            out.append((p, m.group(gi))); gi += 1
        else:
            out.append((p, None))
    return out

def kata2hira(s):
    return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)

class Furi:
    def __init__(self):
        self.d = {}  # kanji_run -> {following_kana_prefix: reading}

    def add(self, word, reading, prio=False):
        a = align(word, reading)
        if not a:
            return
        for i, (p, r) in enumerate(a):
            if r is None:
                continue
            nxt = a[i + 1][0] if i + 1 < len(a) and a[i + 1][1] is None else ''
            slot = self.d.setdefault(p, {})
            key = nxt[:1]
            if prio or key not in slot:
                slot[key] = r

    def annotate(self, s):
        out, i = [], 0
        while i < len(s):
            if not is_kanji(s[i]):
                out.append(s[i]); i += 1; continue
            j = i
            while j < len(s) and is_kanji(s[j]):
                j += 1
            run = s[i:j]
            res = self._run(run, s[j:j + 1])
            out.append(res); i = j
        return ''.join(out)

    def _run(self, run, nxt):
        if run in self.d:
            slot = self.d[run]
            r = slot.get(nxt) or slot.get('') or next(iter(slot.values()))
            return '{%s|%s}' % (run, r)
        # zerlegen: längstes bekanntes Präfix
        for k in range(len(run) - 1, 0, -1):
            if run[:k] in self.d:
                return self._run(run[:k], run[k]) + self._run(run[k:], nxt)
        if len(run) == 1:
            return '{%s|?}' % run
        return self._run(run[0], run[1]) + self._run(run[1:], nxt)
