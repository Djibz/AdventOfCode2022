import re
from math import ceil

with open('input.txt') as iFile:
    hx = hy = tx = ty = 0
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
            dx = hx - tx
            dy = hy - ty
            if dx in [2,-2]:
                tx += dx / 2
                if dy in [1, -1]:
                    ty += dy
            if dy in [2,-2]:
                ty += dy / 2
                if dx in [1, -1]:
                    tx += dx
            visited.append((tx, ty))
    print(visited)
    print(len(set(visited)))
