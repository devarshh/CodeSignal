def solution(young, beautiful, loved):
    if young == False or beautiful == False:
        if loved == True:
            return True
        return False
    if loved == False and young == True and beautiful == True:
        return True
    return False