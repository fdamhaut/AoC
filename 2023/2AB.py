from collections import defaultdict

with open('2.in') as f:
    lines = f.readlines()
lines = [line[line.index(':')+1:].strip() for line in lines]

def one():
    n = 0
    for id, line in enumerate(lines, 1):
        res = defaultdict(lambda: 0)
        for k, v in [l2.split() for l in line.split(';') for l2 in l.split(',')]:
            res[v] = max(res[v], int(k))

        if res['red'] > 12 or res['green'] > 13 or res['blue'] > 14:
            continue
        n += id

    print(n)

def two():
    n = 0
    for id, line in enumerate(lines, 1):
        res = defaultdict(lambda: 0)
        for k, v in [l2.split() for l in line.split(';') for l2 in l.split(',')]:
            res[v] = max(res[v], int(k))

        n += res['red'] * res['green'] * res['blue']

    print(n)

two()