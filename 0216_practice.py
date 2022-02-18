import sys
sys.stdin = open('sample_input (3).txt')

def Palindrome(word):
    rev = ''
    for idx in range(len(word)-1, -1, -1):
        rev += word[idx]
    if rev == word:
        return True
    else:
        return False

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(N):
        word = input()
        if len(word) != M:
            continue
        if Palindrome(word):
            print('#{} {}' .format(TC, word))