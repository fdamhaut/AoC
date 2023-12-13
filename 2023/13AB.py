with open('13.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

patterns, pattern = [], []
for line in lines:
    if not line:
        patterns += [pattern]
        pattern = []
    else:
        pattern += [line]
patterns += [pattern]

def transpose(pattern):
    pattern = zip(*pattern)
    return [''.join(line) for line in pattern]

def check_pattern(pattern, n):
    i = 0
    while 0 <= n-i and n+1+i < len(pattern):
        if pattern[n-i] == pattern[n+1+i]:
            i += 1
        else:
            return False
    return True

def find(pattern, fun):
    for n, line in enumerate(pattern[:-1]):
        if fun(pattern, n):
            return (n+1)*100
    tp = transpose(pattern)
    for n, line in enumerate(tp[:-1]):
        if fun(tp, n):
            return (n+1)
    return 0

print(sum(find(pattern, check_pattern) for pattern in patterns))

def find_diff(s1, s2):
    return [i for i in range(len(s1)) if s1[i] != s2[i]]

def find_smudge(pattern, n):
    diff = False
    i = 0
    while 0 <= n-i and n+1+i < len(pattern):
        d = find_diff(pattern[n - i], pattern[n + 1 + i])
        if not d:
            i += 1
        elif len(d) == 1 and not diff:
            i += 1
            diff = True
        else:
            return False
    return diff


print(sum(find(pattern, find_smudge) for pattern in patterns))
