with open('7.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

class dir:

    def __init__(self, name, p=None):
        self.name = name
        self.size = 0
        self.inside = []
        self.parent = p

    def size_all(self):
        return self.size + sum([i.size_all() for i in self.inside])

    def __str__(self):
        return self.name

first = dir('/')
curr = first

for line in lines[1:]:
    ls = line.split()
    if ls[0] == '$' and ls[1] == 'cd':
        if ls[2] == '..':
            curr = curr.parent
        else:
            curr = dir(ls[2], curr)
            curr.parent.inside += [curr]
    elif ls[0] != 'dir' and ls[0] != '$':
        curr.size += int(ls[0])

q = [first]
res = []

while q:
    node = q.pop()
    q += node.inside
    s = node.size_all()
    if s <= 100000:
        res += [s]

print(sum(res))

need_space = 30000000 - 70000000 + first.size_all()

q = [first]
res = 70000000

while q:
    node = q.pop()
    q += node.inside
    s = node.size_all()
    if need_space <= s < res:
        res = s

print(res)