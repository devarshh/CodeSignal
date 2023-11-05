def solution(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]