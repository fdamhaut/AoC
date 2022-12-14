import numpy as np
with open('14.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

line = lines[0]

minh = 1e20

map = {}

for line in lines:
    poses = [[int(i) for i in pos.split(',')] for pos in line.split(' -> ')]
    curr = poses[0]
    map[tuple(curr)] = 'R'
    for pos in poses[1:]:
        while curr[0] != pos[0]:
            curr[0] += np.sign(pos[0]-curr[0])
            map[tuple(curr)] = 'R'
        while curr[1] != pos[1]:
            curr[1] += np.sign(pos[1]-curr[1])
            map[tuple(curr)] = 'R'

maxh = max(map, key=lambda x:x[1])[1]

def place_sand_A(map):
    s = [500, 0]
    while True:
        if s[1] > maxh:
            return False
        elif (s[0], s[1]+1) not in map:
            s[1] += 1
        elif (s[0]-1, s[1]+1) not in map:
            s = [s[0]-1, s[1]+1]
        elif (s[0]+1, s[1]+1) not in map:
            s = [s[0]+1, s[1]+1]
        else:
            res = s[1] != 0 or tuple(s) not in map
            map[tuple(s)] = 'O'
            return res

score = 0
mapA = map.copy()
while place_sand_A(mapA):
    score += 1

print(score)

def place_sand_B(map):
    s = [500, 0]
    while True:
        if s[1] == maxh+1:
            map[tuple(s)] = 'O'
            return True
        elif (s[0], s[1]+1) not in map:
            s[1] += 1
        elif (s[0]-1, s[1]+1) not in map:
            s = [s[0]-1, s[1]+1]
        elif (s[0]+1, s[1]+1) not in map:
            s = [s[0]+1, s[1]+1]
        else:
            res = s[1] != 0 or tuple(s) not in map
            map[tuple(s)] = 'O'
            return res

score = 0
mapB = map.copy()
while place_sand_B(mapB):
    score += 1

print(score)
