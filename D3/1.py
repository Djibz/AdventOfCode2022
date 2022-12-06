import string

def charValue(c):
    if c in string.ascii_lowercase:
        return ord(c) - 96
    else:
        return ord(c) - 64 + 26

total = 0
with open('input.txt') as iFile:
    for l in iFile:
        a = set(l[:len(l)//2])
        b = set(l[len(l)//2:])
        res = a.intersection(b)
        total += charValue(list(res)[0])

print(total)

last = []
total = 0
with open('input.txt') as iFile:
    count = 0
    for l in iFile:
        l = l[:-1]
        count += 1
        last.append(set(l))
        if count % 3 == 0:
            res = list(last[0].intersection(last[1], last[2]))[0]
            total += charValue(res)
            last = []

print(total)