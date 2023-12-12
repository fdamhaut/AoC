import numpy as np

with open('11.in') as f:
    lines = f.readlines()
lines = [line.strip().split() for line in lines]

mis = [lines[(n*7)+1:(n+1)*7] for n in range((len(lines)+1)//7)]

# TODO make more robust
def make_fun(str):
    if str[2] == 'old':
        return lambda x: x**2
    elif str[1] == '*':
        return lambda x: x*int(str[2])
    else:
        return lambda x: x+int(str[2])

class monkey:
    def __init__(self, obj, op, test_div, t, f):
        self.items = [int(i) for i in obj]
        self.op = make_fun(op)
        self.test_div = int(test_div)
        self.t = int(t)
        self.f = int(f)
        self.act = 0
        self.lcm = 1

    def sort(self):
        # todo Should pop instead ?
        for i in self.items:
            self.act += 1
            v = self.op(i)
            if not v % self.test_div:
                yield self.t, v%lcm
            else:
                yield self.f, v%lcm
        self.items = []

monkeys = []

for mi in mis:
   monkeys += [monkey(
       [s.strip(',') for s in mi[0][2:]], mi[1][3:], mi[2][3], mi[3][5], mi[4][5]
   )]

lcm = np.lcm.reduce([m.test_div for m in monkeys])
for m in monkeys:
    m.lcm = lcm

for round in range(10000):
    for monkey in monkeys:
        for m, v in monkey.sort():
            monkeys[m].items.append(v)

mb = sorted([m.act for m in monkeys], reverse=True)

print(mb, mb[0]*mb[1])