with open('9.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def one():
    res = 0
    for l in lines:
        l = [int(i) for i in l.split()]
        while any(l):
            res += l[-1]
            l = [l[n+1]-l[n] for n in range(len(l)-1)]

    print(res)

def two():
    res = 0
    for l in lines:
        l = [int(i) for i in l.split()]
        m = 1
        while any(l):
            res += m*l[0]
            m *= -1
            l = [l[n+1]-l[n] for n in range(len(l)-1)]

    print(res)

one()
two()
