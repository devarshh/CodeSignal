def solution(inputArray):
    maxString = max(len(s) for s in inputArray)
    returnValue = [s for s in inputArray if len(s) == maxString]
    return returnValue
