import numpy as np
from math import prod

with open('8.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

mapping = [[int(i) for i in line] for line in lines]
mappingp = [list(a) for a in zip(*mapping)]

def compute(line):
    max = -1
    for i in line:
        if i > max:
            yield 1
            max = i
        else:
            yield 0

mv = [np.array(list(compute(line))) + np.array(list(reversed(list(compute(reversed(line)))))) for line in mapping]
mh = [np.array(list(compute(line))) + np.array(list(reversed(list(compute(reversed(line)))))) for line in mappingp]

mh = [list(a) for a in zip(*mh)]

m = [v + np.array(h) for v, h in zip(mv, mh)]

print(sum([1 if a else 0 for line in m for a in line]))


def view_dist(a):
    x, y, h = a
    xm = [v >= h for v in mapping[y][x::-1]]
    xp = [v >= h for v in mapping[y][x:]]
    ym = [v >= h for v in mappingp[x][y:]]
    yp = [v >= h for v in mappingp[x][y::-1]]
    return prod(map(lambda l: l.index(True, 1) if any(l[1:]) else len(l)-1, [xm, xp, ym, yp]))

res = map(view_dist, [(x, y, int(h)) for y, line in enumerate(lines) for x, h in enumerate(line)])

print(max(list(res)))

print(max(list(map(lambda a: prod(map(lambda l: l.index(True, 1) if any(l[1:]) else len(l)-1, [[v >= a[2] for v in map] for map in [mapping[a[1]][a[0]::-1], mapping[a[1]][a[0]:], mappingp[a[0]][a[1]:], mappingp[a[0]][a[1]::-1]]])), [(x, y, int(h)) for y, line in enumerate(lines) for x, h in enumerate(line)]))))
