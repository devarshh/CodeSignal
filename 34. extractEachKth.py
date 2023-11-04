def solution(inputArray, k):
    sol = []
    for i in range(len(inputArray)):
        if (i+1) % k == 0:
            pass
        else:
            sol.append(inputArray[i])
    return sol
