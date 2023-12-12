import numpy as np

with open('9.in') as f:
    lines = f.readlines()
lines = [line.strip().split() for line in lines]

move = {
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
    'R': np.array([1, 0]),
    'L': np.array([-1, 0])
}

cur = np.array([0, 0])
h_pos = [cur:=move[d]*int(v)+cur for d, v in lines]

def sim_rope(h_pos, final=False):
    t = np.array([0, 0])
    yield(t.copy())
    for h in h_pos:
        while not (-1 <= h[0] - t[0] <= 1 and -1 <= h[1] - t[1] <= 1):
            if h[0] != t[0]:
                t[0] += np.sign(h[0] - t[0])
            if h[1] != t[1]:
                t[1] += np.sign(h[1] - t[1])
            yield t.copy()

def sim_ropes(h_pos, length=1):
    for i in range(length):
        h_pos = list(sim_rope(h_pos))
    return h_pos

print(len({tuple(pos) for pos in sim_ropes(h_pos)}))

print(len({tuple(pos) for pos in sim_ropes(h_pos, 9)}))