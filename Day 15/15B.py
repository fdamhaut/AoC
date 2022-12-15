import numpy as np
import math

with open('15.in') as f:
    lines = f.readlines()
lines = [line.strip().split() for line in lines]

sens = []
beac = []

pmax = 4000000

for i in lines:
    xs = int(i[2][2:-1])
    ys = int(i[3][2:-1])
    xb = int(i[8][2:-1])
    yb = int(i[9][2:])
    d = abs(xs-xb) + abs(ys-yb)
    sens += [(xs, ys, d)]
    beac += [(xb, yb)]

def range_no(s, y):
    dist = s[2] - abs(s[1]-y)
    if dist > 0:
        return [(s[0]-dist, +1), (s[0]+dist, -1)]
    elif dist == 0:
        return [(s[0], 0)]
    return []

for y in range(pmax):
    ranges = sorted([n for s in sens for n in range_no(s, y)], key=lambda x: (x[0], -x[1]))
    count = 0
    p = min(ranges[0][0], 0)
    for i in ranges:
        if count == 0:
            if p+1 < i[0]:
                print(f'{y} : [{p+1} : {i[0]-1}]')
                print(y + 4000000 * (p+1))
        p = i[0]
        if p > 4000000:
            break
        count += i[1]

