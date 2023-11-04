def solution(A, B):
    r = []
    for i in range(len(A)):
        if A[i] != B[i]:
            r.append([A[i], B[i]])

    if len(r) == 0 or len(r) == 2 and r[0] == r[1][::-1]:
        return True
    return False