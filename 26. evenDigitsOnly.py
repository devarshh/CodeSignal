def solution(n):
    n_digits = []
    while n > 0:
        rem = n % 10
        n_digits.append(rem)
        n = int(n / 10)
    for i in range(len(n_digits)):
        if n_digits[i] % 2 != 0:
            return False
    return True
