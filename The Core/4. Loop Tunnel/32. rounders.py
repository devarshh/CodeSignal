def solution(n):
    length = len(str(n))
    magnitude = length - 1
    for i in range(length - 1):
        n = int((n / 10) + 0.5)
    return n * (10 ** magnitude)