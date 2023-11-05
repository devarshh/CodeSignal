import itertools
def solution(cell):
    knight_dir = list(itertools.permutations([1,2,-1,-2],2))
    knight_dir1 = []
    valid_moves = 0
    for i in range(len(knight_dir)):
        if sum(knight_dir[i]) != 0:
            knight_dir1.append(knight_dir[i])
    for x,y in knight_dir1:
        if (97 <= ord(cell[0]) + x < 105) and (1 <= int(cell[1]) + y < 9):
            valid_moves +=1
    return valid_moves