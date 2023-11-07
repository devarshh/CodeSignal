def solution(commands):
    count = 0
    smart = 0
    dumb = 0
    for command in commands:
        if command == 'A':
            smart = (smart + 2) % 4
            dumb = (dumb + 2) % 4
        elif command == 'L':
            smart = (smart - 1) % 4
            dumb = (dumb + 1) % 4
        elif command == 'R':
            smart = (smart + 1) % 4
            dumb = (dumb - 1) % 4
        if smart == dumb:
            count += 1
    return count