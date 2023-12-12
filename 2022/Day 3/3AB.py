with open('3.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def prio(chr):
    value = ord(chr)
    return value - 96 if value > 96 else value - 38


score = 0
for line in lines:
    ra = set(line[:len(line) // 2])
    rb = set(line[len(line) // 2:])
    v = ra.intersection(rb)
    score += prio(v.pop())

print(score)

with open('3.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

score = 0
for r in range(len(lines)//3):
    v = set(lines[3*r]).intersection(set(lines[3*r+1])).intersection(set(lines[3*r+2]))
    score += prio(v.pop())

print(score)
