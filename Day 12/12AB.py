with open('12.in') as f:
    lines = f.readlines()
lines = [[ord(i) for i in line.strip()] for line in lines]

mw = len(lines[0])
mh = len(lines)

pos = [i for line in lines for i in line]
start = pos.index(ord('S'))
end = pos.index(ord('E'))
pos[start] = ord('a')
pos[end] = ord('z')


def get_dist(start):
    gone = {}
    for s in start:
        gone[s] = 0
    q = start

    while q:
        p = q.pop(0)

        if p == end:
            return gone[p]

        togo = [] if p % mw == 0 else [p-1]     # L
        togo += [] if p % mw == mw-1 else [p+1] # R
        togo += [] if p < mw else [p-mw]        # U
        togo += [] if p+mw >= len(pos) else [p+mw] # D

        h = pos[p]
        d = gone[p]
        for t in togo:
            if t not in gone and h+1 >= pos[t]:
                gone[t] = d+1
                q += [t]

print(get_dist([start]))

print(get_dist([n for n, a in enumerate(pos) if a == ord('a')]))