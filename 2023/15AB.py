with open('15.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

commands = lines[0].split(',')

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h*=17
        h %= 256
    return h

print(sum(map(hash, commands)))

hm = [[[], set()] for _ in range(256)]

for c in commands:
    i = max(c.find('='), c.find('-'))
    label = c[:i]
    box = hash(label)
    action = c[i]
    fl = int(c[i+1:]) if c[i] == '=' else 0

    if action == '-':
        if label in hm[box][1]:
            hm[box][1].remove(label)
            hm[box][0] = [l for l in hm[box][0] if l[0] != label]
    elif label in hm[box][1]:
        hm[box][0] = [l if l[0] != label else (label, fl) for l in hm[box][0]]
    else:
        hm[box][0] += [(label, fl)]
        hm[box][1].add(label)

res = 0
for nb, box in enumerate(hm, 1):
    for nl, lens in enumerate(box[0], 1):
       res += nb*nl*lens[1]

print(res)