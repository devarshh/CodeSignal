def solution(lastNumberOfDays):
    if lastNumberOfDays == 28 or lastNumberOfDays == 30:
        return [31]
    if lastNumberOfDays == 31:
        return [28, 30, 31]