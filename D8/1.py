matrix = []

with open('input.txt') as iFile:
    for l in iFile:
        matrix.append([int(i) for i in l[:-1]])

def max_of_column(i, j):
    global matrix
    column_top = [matrix[a][j] for a in range(len(matrix)) if a < i]
    column_bot = [matrix[a][j] for a in range(len(matrix)) if a > i]
    return max(column_bot) < matrix[i][j] or max(column_top) < matrix[i][j]

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
            count += 1
            continue
        if max(matrix[i][:j]) < matrix[i][j] or max(matrix[i][j+1:]) < matrix[i][j] or max_of_column(i, j):
            count += 1

print(count)

def scenic_score(x, y):
    global matrix
    v = matrix[x][y]
    r = l = t = b = 1
    if x == len(matrix) - 1:
        r = 0
    else:
        while x + r != len(matrix) - 1 and matrix[x + r][y] < v:
            r += 1

    if x == 0:
        l = 0
    else:
        while matrix[x - l][y] < v and x - l != 0: l += 1

    if y == len(matrix[0]) - 1:
        t = 0
    else:
        while matrix[x][y + t] < v and y + t != len(matrix[0]) - 1: t += 1

    if y == 0:
        b = 0
    else:
        while matrix[x][y - b] < v and y - b != 0: b += 1

    return r * l * t * b

scenics = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        scenics.append(scenic_score(i, j))
print(max(scenics))