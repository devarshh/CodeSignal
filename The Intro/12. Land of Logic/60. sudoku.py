def solution(grid):
    for i in range(0,9):
        if sorted(grid[i]) != list(range(1,10)):
            return False
    for j in range(0,9):
        if sorted(grid[y][j] for y in range(9)) != list(range(1,10)):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if sorted(grid[x][y] for x in range(i,i+3) for y in range(j,j+3)) != list(range(1,10)):
                return False
    return True
