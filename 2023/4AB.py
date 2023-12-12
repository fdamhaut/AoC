from collections import defaultdict

with open('4.in') as f:
    lines = f.readlines()
lines = [line[line.index(':')+1:].strip() for line in lines]

def one():
    n = 0
    for l in lines:
        vals = [set(int(i) for i in j.split()) for j in l.split('|')]
        i = len(vals[0].intersection(vals[1]))
        n += 2**(i-1) if i > 0 else 0

    print(n)

def two():
    extra = defaultdict(lambda: 0)
    for n, l in enumerate(lines):
        total = extra[n] + 1
        vals = [set(int(i) for i in j.split()) for j in l.split('|')]
        i = len(vals[0].intersection(vals[1]))
        for i in range(n+1, n+i+1):
            extra[i] += total
    print(len(lines) + sum(extra.values()))

two()