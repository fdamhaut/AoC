with open('5.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

seeds = [int(i) for i in lines[0][7:].split()]

def one():
    class mapper:

        def __init__(self, to, map, range):
            map, to, range = int(map), int(to), int(range)
            self.range = (map, map+range)
            self.to = to - map

        def map(self, i):
            if self.range[0] <= i < self.range[1]:
                return i + self.to
            return False

        def __repr__(self):
            return repr((self.range, self.to))

        def __str__(self):
            return str((self.range, self.to))

    i = 3
    n = 0
    map = []

    while i < len(lines):
        map += [[]]
        while i < len(lines) and lines[i]:
            map[n] += [mapper(*lines[i].split())]
            i += 1
        i += 2
        n += 1

    locs = []
    for seed in seeds:
        for ms in map:
            ns = seed
            for m in ms:
                if ns:= m.map(seed):
                    seed = ns
                    break
            ns = ns or seed
        locs += [ns]

    print(min(locs))


## TWO

def two():
    class mapper:

        def __init__(self, to, map, range):
            map, to, range = int(map), int(to), int(range)
            self.range = (map, map+range)
            self.to = to - map

        def map(self, fr, to):
            if self.range[0] <= fr < to <= self.range[1]:
                return (fr + self.to, to + self.to), None
            elif self.range[0] <= fr < self.range[1]:
                return (fr + self.to, self.range[1] + self.to), (self.range[1], to)
            elif self.range[0] < to <= self.range[1]:
                return (self.range[0] + self.to, to + self.to), (fr, self.range[0])
            return None, (fr, to)

        def map_list(self, ranges):
            us, ls = [], []
            for r in ranges:
                u, l = self.map(r[0], r[1])
                if u: us += [u]
                if l: ls += [l]
            return us, ls

        def __repr__(self):
            return repr((self.range, self.to))

        def __str__(self):
            return str((self.range, self.to))


    i = 3
    n = 0
    maps = []

    while i < len(lines):
        maps += [[]]
        while i < len(lines) and lines[i]:
            maps[n] += [mapper(*lines[i].split())]
            i += 1
        i += 2
        n += 1

    left = list(zip(seeds[::2], seeds[1::2]))
    left = list(map(lambda x: (x[0], x[0]+x[1]), left))
    used = []

    for transfo in maps:
        left = used + left
        used = []
        for mapper in transfo:
            use, left = mapper.map_list(left)
            used += use

    locs = used + left

    print(min(map(lambda x: x[0], locs)))

two()