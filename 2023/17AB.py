from bisect import insort

with open('17.in') as f:
    lines = f.readlines()
lines = [[int(i) for i in line.strip()] for line in lines]


def tneg(t):
    return tuple(-x for x in t)

direction = ((0, 1), (0, -1), (-1, 0), (1, 0),)     # R0 L1 U2 D3
invert = {0:1, 1:0, 2:3, 3:2}

start = 0, 0, 0, 1
end = (len(lines)-1, len(lines[0])-1)

visited = {}
poses = [(-lines[0][0], start)]

while poses:
    hl, pos = poses.pop(0)
    x, y, d, n = pos

    if n > 3 or pos in visited:
        continue
    if not (0 <= x < len(lines)) or not (0 <= y < len(lines[0])):
        continue
    visited[pos] = hl
    hl += lines[x][y]
    if (x, y) == end:
        print(hl)
        break
    for nu, (x2, y2) in enumerate(direction):
        if nu == invert[d]:
            continue
        insort(poses, (hl, (x+x2, y+y2, nu, 1 if nu != d else n+1)))


visited = {}
poses = [(-lines[0][0], start)]

while poses:
    hl, pos = poses.pop(0)
    x, y, d, n = pos

    if n > 10 or pos in visited:
        continue
    if not (0 <= x < len(lines)) or not (0 <= y < len(lines[0])):
        continue
    visited[pos] = hl
    hl += lines[x][y]
    if (x, y) == end:
        print(hl)
        break
    for nd, (x2, y2) in enumerate(direction):
        if nd == invert[d] or (nd != d and n < 4):
            continue
        insort(poses, (hl, (x+x2, y+y2, nd, 1 if nd != d else n+1)))
