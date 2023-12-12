from collections import defaultdict

with open('7.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def one():
    def h2val(h):
        h = h.replace('T', 'a').replace('J', 'b').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
        dd = defaultdict(lambda: 0)
        for c in h:
            dd[c] += 1

        vals = sorted(dd.values(), reverse=True)
        if vals[0] == 5:
            return 6, h
        elif vals[0] == 4:
            return 5, h
        elif vals[0] == 3:
            return 3 + (vals[1] == 2), h
        elif vals[0] == 2:
            return 1 + (vals[1] == 2), h
        return 0, h


    di = dict()

    for l in lines:
        hand, bet = l.split()
        di[h2val(hand)] = int(bet)

    res = 0
    for n, (k, v) in enumerate(sorted(di.items()), 1):
        res += v*n

    print(res, sorted(di.items()))

def two():
    def h2val(h):
        h = h.replace('T', 'a').replace('J', '0').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
        dd = defaultdict(lambda: 0)
        for c in h:
            dd[c] += 1

        j = 0
        if len(dd) > 1 and '0' in dd:
            j = dd['0']
            del dd['0']

        vals = sorted(dd.values(), reverse=True)
        if vals[0] + j == 5:
            return 6, h
        elif vals[0] + j == 4:
            return 5, h
        elif vals[0] + j == 3:
            return 3 + (vals[1] == 2), h
        elif vals[0] + j == 2:
            return 1 + (vals[1] == 2), h
        return 0, h

    di = dict()

    for l in lines:
        hand, bet = l.split()
        di[h2val(hand)] = int(bet)

    res = 0
    for n, (k, v) in enumerate(sorted(di.items()), 1):
        res += v * n

    print(res, sorted(di.items()))

two()