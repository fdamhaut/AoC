with open('16.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


direction = ((0, 1), (0, -1), (-1, 0), (1, 0),)     # R0 L1 U2 D3
special = {
    '/': {0:[2], 2:[0], 1:[3], 3:[1]},
    '\\': {0:[3], 3:[0], 1:[2], 2:[1]},
    '-': {2:[0, 1], 3:[0, 1]},
    '|': {0: [2, 3], 1: [2, 3]},
    '.': {}
}

def energize(start):
    visited = set()
    poses = [start]

    while poses:
        x, y, d = poses.pop()
        if (x, y, d) in visited:
            continue
        elif not (0 <= x < len(lines)) or not (0 <= y < len(lines[0])):
            continue
        visited.add((x, y, d))
        nds = special[lines[x][y]].get(d, [d])
        poses += [(x+direction[nd][0], y+direction[nd][1], nd) for nd in nds]

    vis_pos = set((x, y) for x, y, d in visited)
    return len(vis_pos)

print(energize((0, 0, 0)))

starts = [(x, 0, 0) for x in range(len(lines))]
starts += [(x, len(lines[0])-1, 1) for x in range(len(lines))]
starts += [(0, y, 3) for y in range(len(lines[0]))]
starts += [(len(lines)-1, y, 2) for y in range(len(lines[0]))]

print(max(map(energize, starts)))