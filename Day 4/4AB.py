with open('4.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

score = 0
for line in lines:
    a1, a2, b1, b2 = [int(x) for l in line.split(',') for x in l.split('-')]
    score += 1 if a1 <= b1 <= b2 <= a2 or b1 <= a1 <= a2 <= b2 else 0

print(score)
print(sum(list(map(lambda x: 1 if x[0] <= x[2] <= x[3] <= x[1] or x[2] <= x[0] <= x[1] <= x[3] else 0, list(map(lambda line: [int(x) for l in line.split(',') for x in l.split('-')], [line.strip() for line in open('4.in').readlines()]))))))


with open('4.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

score = 0
for line in lines:
    a1, a2, b1, b2 = [int(x) for l in line.split(',') for x in l.split('-')]
    score += 0 if a1 <= a2 < b1 <= b2 or b1 <= b2 < a1 <= a2 else 1

print(score)

print(sum(list(map(lambda x: 0 if x[1] < x[2] or x[3] < x[0] else 1, list(map(lambda line: [int(x) for l in line.split(',') for x in l.split('-')], [line.strip() for line in open('4.in').readlines()]))))))
