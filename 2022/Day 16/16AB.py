from collections import defaultdict
from time import time
import sys
sys.setrecursionlimit(10**6)

with open('16.in') as f:
    lines = f.readlines()
lines = [line.strip().split() for line in lines]

pumps = {}

for id, l in enumerate(lines):
    pos = l[1]
    rate = int(l[4][5:-1])
    lead = [v.strip(',') for v in l[9:]]
    pumps[pos] = [rate, lead, {}]

def get_dist(pos):
    seen = {}
    q = [(pos, 0)]
    while q:
        p = q.pop(0)
        seen[p[0]] = p[1]
        q += [(np, p[1]+1) for np in pumps[p[0]][1] if np not in seen]
    pumps[pos][2] = {p:d for p, d in seen.items() if pumps[p][0] > 0}

[get_dist(pos) for pos in pumps]

store = defaultdict(lambda: defaultdict(lambda: {}))

def compute(pos, time, open):
    if time < 2:
        return 0

    if pumps[pos][0]:
        time -= 1
        here = time * pumps[pos][0]
        if here < 0:
            return 0
    else:
        here = 0

    open = open.copy()
    open.add(pos)
    openhash = "".join(sorted(open))

    if time in store[pos] and openhash in store[pos][time]:
        return store[pos][time][openhash]

    v = max([0]+[compute(p, time-d, open) for p, d in pumps[pos][2].items() if p not in open]) + here
    store[pos][time][openhash] = v
    return v


start = time()
print(compute('AA', 30, set()))
print(time()-start)