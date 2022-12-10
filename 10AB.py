with open('10.in') as f:
    lines = f.readlines()
lines = [line.strip().split() for line in lines]

X = 1

noop = lambda x: x[0]
addx = lambda x: x[0] + int(x[1])

act = {
    'noop': [noop],
    'addx': [noop, addx]
}


timer = 1
x = 1

res = 0

all = [1]
for line in lines:
    for action in act[line[0]]:
        x = action([x]+line[1:])
        timer += 1
        all += [x]
        if timer % 40 == 20:
            res += timer*x

print(res)

draw = ['#' if v-1 <= n % 40 <= v+1 else ' ' for n, v in enumerate(all)]

for i in range(len(draw)//40):
    print(''.join(draw[40*i:40*(i+1)]))