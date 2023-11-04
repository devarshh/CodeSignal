def solution(st):
    for i in range(len(st)):
        sub_str = st[i:len(st)]
        if sub_str[::-1] == sub_str:
            missing = st[0:i]
            return st + missing[::-1]
    return st
