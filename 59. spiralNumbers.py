def solution(n):
    dims = n
    elem = 1
    matrix = [[0]*n for x in range(n)]
    while 0 < dims:
        i = n - dims
        for j in range(n - dims, dims):
            matrix[i][j] = elem
            elem += 1
        for i in range(n - dims +1, dims):
            matrix[i][j] = elem
            elem += 1
        for j in range(dims - 2, n - dims - 1, -1):
            matrix[i][j] = elem
            elem += 1
        for i in range(dims - 2, n - dims, -1):
            matrix[i][j] = elem
            elem += 1
        dims -= 1
    return matrix