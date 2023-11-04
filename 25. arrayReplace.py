def solution(inputArray, elemToReplace, substitutionElem):
    newArray = []
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            newArray.append(substitutionElem)
        else:
            newArray.append(inputArray[i])
    return newArray