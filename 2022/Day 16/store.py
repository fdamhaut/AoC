from collections import defaultdict
from time import time

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
    pumps[pos][2] = {p:d for p, d in seen.items() if pumps[p][0] > 0 and p != pos}

[get_dist(pos) for pos in pumps]

for p in pumps:
    if pumps[p][0] or p == 'AA':
        print(p, pumps[p][0],  pumps[p][2])

def compute(pos, time, open):
    if pumps[pos][0]:
        time -= 1
        here = time * pumps[pos][0]
    else:
        here = 0

    open = open.copy()
    open.add(pos)

    v = here
    for p, d in pumps[pos][2].items():
        if p not in open and d < time:
            res=compute(p, time-d, open) + here
            v = max(res, v)
    return v

start = time()
print(compute('AA', 30, set()))
print(time()-start)