with open('1.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

elf = []
current = 0
for line in lines:
    if not line:
        elf += [current]
        current = 0
    else:
        current += int(line)

print(max(elf))
print(sum(sorted(elf)[-3:]))