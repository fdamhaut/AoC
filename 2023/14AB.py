with open('14.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

cols = list(zip(*lines))

def load(cols):
    l = len(cols[0])
    res = 0
    for col in cols:
        d = 0
        for n, c in enumerate(col):
            if c == '#': d = n+1
            elif c == 'O':
                res += l - d
                d += 1
    return res

print(load(cols))

def remap(lines):
    d = {'.': 0, '#': 1, 'O':2}
    return [list(map(lambda x: d[x], line)) for line in lines]

def tostr(lines):
    return ''.join([''.join(map(str, n)) for n in lines])

def rotate(lines):
    return [list(reversed(l)) for l in list(zip(*lines))]

def slide(lines):
    res = []
    for line in lines:
        newcol = [0]*len(line)
        d = 0
        for n, c in enumerate(line, 1):
            if c == 1:
                newcol[n-1] = 1
                d = n
            elif c == 2:
                newcol[d] = 2
                d += 1
        res += [newcol]
    return res

saved = dict()
def cycle(m, n=1e9):
    n = int(n)
    i = 0
    done = False
    while i < n:
        if not done and (s:=tostr(m)) in saved:
            done = True
            n = i + (n-i)%(i-saved[s])
        elif not done:
            saved[s] = i
        for _ in range(4):
            m = slide(m)
            m = rotate(m)
        i += 1
    return m

def load_no_slide(cols):
    l = len(cols[0])
    res = 0
    for col in cols:
        for n, c in enumerate(col):
            if c == 2: res += l-n
    return res

s = rotate(rotate(rotate(remap(lines))))

print(load_no_slide(cycle(s)))
