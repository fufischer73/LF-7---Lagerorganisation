import sys
def P(f, pairs):
    s = open(f).read()
    for a, b in pairs:
        n = s.count(a)
        assert n == 1, (f, n, a[:70])
        s = s.replace(a, b)
    open(f, 'w').write(s)
