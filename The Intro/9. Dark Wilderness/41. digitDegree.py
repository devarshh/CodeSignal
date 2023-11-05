def solution(n):
    degree = 0
    while n >= 10:
        num = str(n)
        n = sum(int(i) for i in num)
        degree +=1
    return degree