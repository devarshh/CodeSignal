def solution(time):
    time_split = time.split(":")
    if int(time_split[0]) < 24 and 00 <= int(time_split[1]) <= 59:
        return True
    else:
        return False