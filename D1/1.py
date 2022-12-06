elfs = []
tmpElf = 0
with open('input.txt') as iFile:
    for l in iFile:
        if l == '' or l == '\n':
            elfs.append(tmpElf)
            tmpElf = 0
        else:
            tmpElf += int(l)

print(max(elfs))

elfs.sort()

print(elfs[-1] + elfs[-2] + elfs[-3])