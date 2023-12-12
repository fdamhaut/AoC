from itertools import combinations

with open('11.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

galaxies = []
doublel = []
doublec = []

for i, l in enumerate(lines):
    dl = True
    for j, c in enumerate(l):
        if c == '#':
            dl = False
            galaxies += [(i, j)]
    if dl:
        doublel += [i]

for i, l in enumerate(zip(*lines)):
    if l.count('.') == len(l):
        doublec += [i]

distl = sorted(doublel + list(range(len(lines))))
distc = sorted(doublec + list(range(len(lines[0]))))


def getdist(a, b, dist, m=1000000):
    return abs(a-b) + (m-1) * (abs(dist.index(a) - dist.index(b)) - abs(a-b))

res = 0
for g1, g2 in combinations(galaxies, 2):
    res += getdist(g1[0], g2[0], distl)
    res += getdist(g1[1], g2[1], distc)

print(res)
