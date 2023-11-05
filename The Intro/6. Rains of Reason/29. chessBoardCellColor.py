def solution(cell1, cell2):
    cell1_total = ord(cell1[0]) + int(cell1[1])
    cell2_total = ord(cell2[0]) + int(cell2[1])
    if (cell1_total + cell2_total) % 2 == 0:
        return True
    else:
        return False