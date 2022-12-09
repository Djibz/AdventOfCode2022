with open('input.txt') as iFile:
    line = iFile.read()
    idx = 14
    print(len(list(set(line[idx-14:idx]))))
    while len(list(set(line[idx-14:idx]))) != 14:
        idx += 1
    print(idx)