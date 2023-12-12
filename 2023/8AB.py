from collections import defaultdict

with open('8.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
path = lines[0]
nodes = lines[2:]

class nodeC:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def next(self, c):
        return self.left if c == 'L' else self.right

ndict = {}
for node in nodes:
    node = node.split()
    ndict[node[0]] = nodeC(node[2].strip('(),'), node[3].strip('(),'))

def pathgen(i, start=''):
    for c in start:
        yield c
    while True:
        for c in i:
            yield c

def pathgenn(i, start=''):
    for c in start:
        yield c, None
    while True:
        for n, c in enumerate(i):
            yield c, n


pathg = pathgen(path)

def one(path=pathg):
    n = 0
    node = 'AAA'

    while node != 'ZZZ':
        node = ndict[node].next(next(path))
        n += 1

    print(n)

# one()

generators = []
nodes = [n for n in ndict if n[2] == 'A']

for node in nodes:
    seen = defaultdict(dict)
    i = 0
    p = [0]*int(1e6)
    for c, n in pathgenn(path):
        if n in seen[node]:
            generators += [p.index(True)]
            break
        p[i] = node[2] == 'Z'
        seen[node][n] = i
        i += 1
        node = ndict[node].next(c)

def ppcm(x, y):
    if y > x:
        return ppcm(y, x)
    if not x % y:
        return y
    return ppcm(y, x % y)

def pgcd(x, y):
    return x*y//ppcm(x,y)


res = generators[0]
for n in generators[1:]:
    res = pgcd(res, n)

print(res)