with open('10.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

map = {}
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == 'S':
            S = i, j
        map[(i, j)] = c

adj = [(-1, 0, 's'), (1, 0, 'n'), (0, -1, 'e'), (0, 1, 'w')]

next = {
    '|': {'n': (1, 0, 'n'), 's': (-1, 0, 's')},
    '-': {'e': (0, -1, 'e'), 'w': (0, 1, 'w')},
    'L': {'n': (0, 1, 'w'), 'e': (-1, 0, 's')},
    'J': {'n': (0, -1, 'e'), 'w': (-1, 0, 's')},
    '7': {'s': (0, -1, 'e'), 'w': (1, 0, 'n')},
    'F': {'s': (0, 1, 'w'), 'e': (1, 0, 'n')},
    '.': {},
}

def loop(S, path):
    pos = S
    loop = [S]

    while True:
        pos = pos[0] + path[0], pos[1] + path[1]
        loop += [pos]
        if not (c := map.get(pos, False)):
            break
        if c == 'S':
            return loop
        if not (path := next[c].get(path[2], False)):
            break


for a in adj:
    l = loop(S, a)
    if l:
        print(len(l)//2)
        break


ls = set(l)
lines = [list(l) for l in lines]
lines[S[0]][S[1]] = 'F'

switch, semi, check, lines = {'|'}, {'J', '7'}, {'F':'J', 'L':'7'}, lines

r = 0
for i, l in enumerate(lines):
    inside = False
    toswitch = False
    for j, c in enumerate(l):
        if inside and (i, j) not in ls: r += 1
        elif (i, j) not in ls: continue
        elif c in switch: inside = not inside
        elif c in semi:
            if toswitch == c: inside = not inside
            toswitch = False
        elif c in check: toswitch = check[c]
print(r)