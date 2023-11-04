def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if max(yourLeft, yourRight) == max(friendsRight, friendsLeft) and min(yourLeft, yourRight) == min(friendsLeft, friendsRight):
        return True
    else:
        return False
