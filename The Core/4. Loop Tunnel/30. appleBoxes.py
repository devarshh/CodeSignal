def solution(k):
    red_apple_count = 0
    yellow_apple_count = 0
    for i in range(1, k + 1, 2):
        yellow_apple_count += i * i
    for i in range(2, k + 1, 2):
        red_apple_count += i * i
    return (red_apple_count - yellow_apple_count)