def solution(inputArray):
    length = len(inputArray)
    sum = []
    for i in range(length-1):
        sum.append(inputArray[i] * inputArray[i+1])
    return max(sum)