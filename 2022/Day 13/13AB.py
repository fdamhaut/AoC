from functools import cmp_to_key

with open('13.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def cp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, list) and isinstance(b, list):
        for xa, xb in zip(a, b):
            if r:=cp(xa, xb):
                return r
        return len(a) - len(b)
    elif isinstance(a, list):
        return cp(a, [b])
    else:
        return cp([a], b)


score = 0
for i in range(len(lines)//3+1):
    a = eval(lines[i*3])
    b = eval(lines[i*3+1])
    if cp(a, b) <= 0:
        score += i+1

print(score)

lst = [[[2]], [[6]]]
for i in range(len(lines)//3+1):
    lst += [eval(lines[i*3])]
    lst += [eval(lines[i*3+1])]

lst = sorted(lst, key=cmp_to_key(cp))

print((lst.index([[2]])+1)*(lst.index([[6]])+1))