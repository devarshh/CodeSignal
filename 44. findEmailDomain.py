def solution(address):
    split_add = address.split("@")
    domain_part = [i for i in split_add]
    if len(split_add) == 2:
        return domain_part[1]
    if len(split_add) == 3:
        return domain_part[2]