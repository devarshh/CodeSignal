def solution(bishop, pawn):
    if ord(bishop[0]) == ord(pawn[0]):
        return False
    else:
        bishop_total = ord(bishop[0]) + int(bishop[1])
        pawn_total = ord(pawn[0]) + int(pawn[1])
        return (bishop_total + pawn_total) % 2 == 0