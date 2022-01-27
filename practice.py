n = int(input())
for i in range(n):
    lst = input()
    total = 0
    basic_score = 1
    for char in lst:
        if char == 'O':
            total += basic_score
            basic_score += 1
        if char == 'X':
            basic_score = 1
    print(total)