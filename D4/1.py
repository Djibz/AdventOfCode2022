import re

with open('input.txt') as iFile:
    count = 0
    count2 = 0
    for l in iFile:
        a, b, c, d = re.findall(r'[0-9]+', l)
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if (a >= c and b <= d) or (c >= a and d <= b):
            count += 1
        if (a >= c and a <= d) or (c >= a and c <= b):
            count2 += 1
    print(count)
    print(count2)
