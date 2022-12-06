score = 0
with open('input.txt') as iFile:
    for l in iFile:
        a = l[0]
        b = l[2]
        if b == 'X':
            score += 1
            if a == 'A':
                score += 3
            if a == 'C':
                score += 6
        if b == 'Y':
            score += 2
            if a == 'A':
                score += 6
            if a == 'B':
                score += 3
        if b == 'Z':
            score += 3
            if a == 'B':
                score += 6
            if a == 'C':
                score += 3

print(score)

score = 0
with open('input.txt') as iFile:
    for l in iFile:
        a = l[0]
        b = l[2]
        if b == 'X':
            if a == 'A':
                score += 3
            if a == 'B':
                score += 1
            if a == 'C':
                score += 2
        if b == 'Y':
            score += 3
            if a == 'A':
                score += 1
            if a == 'B':
                score += 2
            if a == 'C':
                score += 3
        if b == 'Z':
            score += 6
            if a == 'A':
                score += 2
            if a == 'B':
                score += 3
            if a == 'C':
                score += 1

print(score)
