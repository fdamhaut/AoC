import sys
import functools

sys.setrecursionlimit(int(1e6))

with open('12.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def simplify(l):
    first = True
    for c in l:
        if c == '.' and not first:
            yield '.'
            first = True
        elif c != '.':
            yield c
            first = False


l2 = [l.split() for l in lines]
lines = [(''.join(simplify(s)).strip('.').split('.'), list(int(j) for j in c.split(','))) for s, c in l2]
lines2 = [(''.join(simplify(s*5)).strip('.').split('.'), list(int(j) for j in c.split(','))*5) for s, c in l2]

@functools.lru_cache(maxsize=None)
def canfit(s, v, sv=False):
    sv = sv or (sum(v) + len(v) - 1)
    if len(s) < sv:
        return 0
    elif not s and sv <= 0:
        return 1
    elif v and len(s) == v[0]:
        return 1
    res = 0
    if s[0] == '?':
        res += canfit(s[1:], v, sv)
    if v and s[v[0]] == '?':
        res += canfit(s[v[0]+1:], v[1:], sv-v[0]-1)
    return res

@functools.lru_cache(maxsize=None)
def groups(l, n, s):
    if n == 1:
        return [[tuple(l)]]
    if not l:
        return [[tuple() for _ in range(n)]]
    res = []
    maxval = len(s[0])
    for i in range(len(l)+1):
        t = tuple(l[:i])
        if sum(t)+len(t)-1 > maxval:
            break
        for j in groups(l[i:], n-1, s[1:]):
            res += [[t] + j]
    return res

def solve(s, v):
    res = 0
    for gs in groups(tuple(v), len(s), tuple(s)):
        r = 1
        for su, g in zip(s, gs):
            r *= canfit(su, g)
        res += r
    return res

print(sum(solve(s, v) for s, v in lines))

res = 0
for n, (s, v) in enumerate(lines2, 1):
    print(n)
    res += solve(s, v)

print(res)
