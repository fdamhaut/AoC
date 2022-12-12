with open('5.in') as f:
    lines = f.readlines()
lines = [line.strip('\n') for line in lines]

NSTACK = 9
STACK_H = 8

stacks = [[] for i in range(NSTACK)]

for i in range(STACK_H):
    line = lines.pop(0)
    for n, stack in enumerate(stacks):
        index = 1+4*n
        if len(line) > index:
            stack += [line[index]] if line[index] != " " else []

# We stored top to bottom, we want top at the end
[s.reverse() for s in stacks]

# remove 2 useless lines
lines.pop(0)
lines.pop(0)

for line in lines:
    _, move, _, f, _, t = line.split()
    move, f, t = int(move), int(f)-1, int(t)-1
    stacks[t] += stacks[f][-move:]
    stacks[f] = stacks[f][:-move]

score = [s.pop() for s in stacks]
print("".join(score))
