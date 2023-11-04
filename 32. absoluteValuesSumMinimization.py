def solution(a):
    sums = []
    for i in range(len(a)):
        summ = 0
        for j in range(len(a)):
            summ += abs(a[i] - a[j])
        sums.append(summ)
    return a[sums.index(min(sums))]