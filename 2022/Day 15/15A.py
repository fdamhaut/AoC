import numpy as np
import math

with open('15.demo') as f:
    lines = f.readlines()
lines = [line.strip().split() for line in lines]

sens = []
beac = []

ytest = 10

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

ranges = sorted([n for s in sens for n in range_no(s, ytest)], key=lambda x: (x[0], -x[1]))

score = 0
count = 0

for i in ranges:
    if count > 0:
        score += i[0] - p
    else:
        if p+1 < i[0]:
            print(f'[{p+1} : {i[0]+1}]')
        score += 1
    p = i[0]
    count += i[1]

existing = set()
for b in beac:
    if b[1] == ytest:
        existing.add(b[0])

print(score - len(existing))