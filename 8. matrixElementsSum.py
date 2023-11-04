def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    total=0
    for j in range(col):
        for i in range(row):
            if matrix[i][j]!=0:
                total+=matrix[i][j]
            else:
                break
    return total
