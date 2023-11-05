def solution(inputString):
    alpnums = inputString.split("-")
    count = 0
    if len(alpnums) != 6:
        return False
    if len(inputString) != 17:
        return False
    for i in range(0,6):
        if alpnums[i] == "":
            return False
        if re.search('[a-zG-Z]',alpnums[i]):
            count += 1
            if count > 0:
                return False
    return True