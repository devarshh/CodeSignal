def solution(a, b, n):
    dollars = 0
    for i in range(n):
        dollars += (a * b)
        a += 1
        b += 1
    return dollars
