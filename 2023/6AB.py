from math import sqrt, ceil

with open('6.in') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
times = lines[0][lines[0].index(':')+1:].split()
distances = lines[1][lines[1].index(':')+1:].split()


def one():
    s = 1
    for t, d in zip(times, distances):
        t, d = int(t), int(d)
        b = (t - sqrt(t**2-4*d))/2
        res = (t + 1) - 2 * ceil(b+1e-5)
        s *= res
    print(s)

def two():
    s = 1
    times = lines[0][lines[0].index(':') + 1:].split()
    distances = lines[1][lines[1].index(':') + 1:].split()
    times = ["".join(times)]
    distances = ["".join(distances)]
    for t, d in zip(times, distances):
        t, d = int(t), int(d)
        b = (t - sqrt(t**2-4*d))/2
        res = (t + 1) - 2 * ceil(b+1e-5)
        s *= res
    print(s)

two()
