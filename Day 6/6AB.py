with open('6.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
line = lines[0]

print(list(map(lambda n:len(set(line[n:n+4])), range(len(line)-4))).index(4)+4)
print(list(map(lambda n:len(set(line[n:n+14])), range(len(line)-14))).index(14)+14)