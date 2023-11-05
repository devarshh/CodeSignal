def solution(s):
    res = ""
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count+=1
        elif (s[i] != s[i+1]) and count >= 2:
            res += str(count) + s[i]
            count = 1
        elif (s[i] != s[i+1]):
            res += s[i]
            count =1
        if ((i+1) == len(s)-1) and (s[i] != s[i+1]):
            res += s[i+1]
        elif ((i+1) == len(s)-1) and (s[i] == s[i+1]):
            res += str(count) + s[i+1]
    return res
