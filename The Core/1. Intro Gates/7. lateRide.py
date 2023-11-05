def solution(n):
    hours = int(n / 60)
    minutes = n % 60
    temp = 0
    while minutes:
        temp += minutes % 10
        minutes //= 10
    while hours:
        temp += hours % 10
        hours //= 10
    return temp
