def solution(inputString):
    freq = {}
    for c in inputString:
        freq[c] = freq.get(c, 0) + 1
    num_odd_freq = 0
    for count in freq.values():
        if count % 2 != 0:
            num_odd_freq += 1
        if num_odd_freq > 1:
            return False
    return True