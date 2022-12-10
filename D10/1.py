import re

cycle = 1
x = 1
e = [20, 60, 100, 140, 180, 220]
total = 0
s = ['#' for i in range(240)]

def write():
    global cycle, x, s
    c = cycle%40
    if c >= x and c < x+3:
        s[cycle - 1] = '#'
    else:
        s[cycle - 1] = '.'

with open('input.txt') as iFile:
    for l in iFile:
        write()
        if cycle in e:
                total += x * cycle
        if 'noop' in l:
            cycle += 1
        else:
            cycle += 1
            write()
            if cycle in e:
                total += x * cycle
            cycle += 1
            x += int(re.findall(r'-?[0-9]+', l)[0])
            #<3
print(x)
print(total)
for i in range(len(s)):
    if i % 40 == 0:
        print('')
    print(s[i], end='')
    