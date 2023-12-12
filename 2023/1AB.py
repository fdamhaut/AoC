import re

with open('1.in') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

chars = ''.join(map(chr, range(ord('a'), ord('z')+1)))
digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def reverse(str):
    return ''.join(list(reversed(str)))

inverted = {reverse(k):v for k, v in digits.items()}

def one():
    n = 0
    for line in lines:
        l = line.strip(chars)
        n += int(l[0]+l[-1])
    print(n)


def replace(digits):
    return lambda x : digits[x.string[x.regs[0][0]:x.regs[0][1]]]
def two():
    n = 0
    for line in lines:
        l = re.sub('|'.join(digits), replace(digits), line).strip(chars)
        li = re.sub('|'.join(inverted), replace(inverted), reverse(line)).strip(chars)
        n += int(l[0] + li[0])
    print(n)


two()
