import re
from math import ceil

with open('input.txt') as iFile:
    hx = hy = 0
    x = [0 for _ in range(9)]
    y = [0 for _ in range(9)]
    visited = []
    for l in iFile:
        command = l[0]
        nb = int(re.findall(r"[0-9]+", l)[0])
        for _ in range(nb):
            if command == 'U':
                hy += 1
            if command == 'D':
                hy -= 1
            if command == 'R':
                hx += 1
            if command == 'L':
                hx -= 1
            for i in range(9):
                if i == 0:
                    px, py = hx, hy
                else:
                    px, py = x[i-1], y[i-1]
                dx = px - x[i]
                dy = py - y[i]
                if dx in [2,-2]:
                    x[i] += dx / 2
                    if dy in [1, -1]:
                        y[i] += dy
                if dy in [2,-2]:
                    y[i] += dy / 2
                    if dx in [1, -1]:
                        x[i] += dx
            visited.append((x[-1], y[-1]))
    print(visited)
    print(len(set(visited)))
