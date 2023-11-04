def solution(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    square = []
    square_no = 0
    for i in range(rows - 1):
        for j in range(col-1):
            sq_2by2 = [ matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1] ]
            if sq_2by2 not in square:
                square.append(sq_2by2)
                square_no += 1
    return square_no
