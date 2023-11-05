def solution(min1, min2_10, min11, s):
    if s < min1:
        return 0
    for i in range(2, 11):
        if s < min1 + min2_10 * (i - 1):
            return i - 1
    return (s - min1 - min2_10 * 9.0) //min11 + 10