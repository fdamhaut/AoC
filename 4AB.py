with open('4.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

score = 0
for line in lines:
    a1, a2, b1, b2 = [int(x) for l in line.split(',') for x in l.split('-')]
    score += 1 if a1 <= b1 <= b2 <= a2 or b1 <= a1 <= a2 <= b2 else 0

print(score)

with open('4.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

score = 0
for line in lines:
    a1, a2, b1, b2 = [int(x) for l in line.split(',') for x in l.split('-')]
    score += 0 if a1 <= a2 < b1 <= b2 or b1 <= b2 < a1 <= a2 else 1

print(score)