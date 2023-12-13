from collections import defaultdict
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

def groups(l, n):
    if n == 1:
        yield [tuple(l)]
        return
    if not l:
        yield [tuple() for _ in range(n)]
        return
    for i in range(len(l)+1):
        t = tuple(l[:i])
        for j in groups(l[i:], n-1):
            yield [t] + j
def solve(s, v):
    res = 0
    for gs in groups(v, len(s)):
        r = 1
        for su, g in zip(s, gs):
            r *= canfit(su, g)
        res += r
    return res

# print(lines)
# print(canfit('???', [1, 1]))
#
# res = [(s, v, solve(s, v)) for s, v in lines]

print(sum(solve(s, v) for s, v in lines))

res = 0
for n, (s, v) in enumerate(lines2):
    print(n, s, v)
    res += solve(s*5, v*5)

print(res)
