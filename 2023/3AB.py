with open('3.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

class label:
    def __init__(self, pos, val):
        self.used = False
        self.pos = pos
        self.val = val

    def __repr__(self):
        return str(self.val) + str(self.pos)

    def __hash__(self):
        return hash(pos[0])

labels = []
sym = []

for x, line in enumerate(lines):
    i = ''
    pos = []
    for y, c in enumerate(line):
        if c.isdigit():
            i += c
            pos += [(x, y)]
        else:
            labels += [label(pos, int(i))] if i else []
            pos, i = [], ''
            if c != '.':
                sym += [(x, y, c)]
    labels += [label(pos, int(i))] if i else []

pos2label = dict()
for l in labels:
    for pos in l.pos:
        pos2label[pos] = l

def one():
    for s in sym:
        for x2, y2 in [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]:
            if (s[0]+x2, s[1]+y2) in pos2label:
                pos2label[(s[0]+x2, s[1]+y2)].used = True

    print(sum([l.val for l in labels if l.used]))

def two():
    n = 0
    for s in sym:
        if s[2] != '*':
            continue
        ls = set()
        for x2, y2 in [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]:
            if (s[0] + x2, s[1] + y2) in pos2label:
                ls.add(pos2label[(s[0] + x2, s[1] + y2)])
        ls = list(ls)
        if len(ls) == 2:
            n += ls[0].val * ls[1].val
    print(n)

two()