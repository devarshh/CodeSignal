def solution(inputArray):
    for i in range(len(inputArray)):
        if i == 0:
            cnt = 0
        elif abs(inputArray[i] - inputArray[i-1]) >= cnt:
            cnt = abs(inputArray[i] - inputArray[i-1])
    return cnt
