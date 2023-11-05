def solution(n):
    num = str(n)
    sol_n = list(int("".join(num[:i] + num[i+1:])) for i in range(len(num)))
    return max(sol_n)