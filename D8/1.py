matrix = []

with open('inputtest.txt') as iFile:
    for l in iFile:
        matrix.append([int(i) for i in l[:-1]])

def max_of_column(i, j):
    global matrix
    column_top = [matrix[a][j] for a in range(len(matrix)) if a < i]
    column_bot = [matrix[a][j] for a in range(len(matrix)) if a > i]
    return max(column_bot) < matrix[i][j] or max(column_top) < matrix[i][j]
    return True

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
            count += 1
            continue
        if max(matrix[i][:i]) < matrix[i][j] or max(matrix[i][i+1:]) < matrix[i][j] or max_of_column(i, j):
            count += 1

print(count)