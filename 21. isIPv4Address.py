import ipaddress
def solution(inputString):
    try:
        ipaddress.ip_address(inputString)
    except:
        return False
    return True
