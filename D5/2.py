import re

stacks = [[] for i in range(10)]
moves = []

with open('input.txt') as iFile:
    for l in iFile:
        if '[' in l:
            s = len(l)
            i = 0
            while 1 + i * 4 < s:
                c = l[1 + i * 4]
                if c != ' ':
                    stacks[i].insert(0, c)
                i+=1
        if l[:4] == 'move':
            nb, a, b = [int(num) for num in re.findall(r'[0-9]+', l)]
            moves.append([nb, a, b])

for m in moves:
    poped = []
    for i in range(m[0]):
        poped.append(stacks[m[1]-1].pop())
    poped.reverse()
    for p in poped:
        stacks[m[2]-1].append(p)

s = ''
for st in stacks:
    if len(st):
        s += st[-1]
print(s)