import sys
sys.stdin = open('회문1.txt', 'r')

T = 10

for test_case in range(1,T+1):
    N = int(input())
    matrix = []
    cnt = 0
    for _ in range(8):
        word = list(input())
        matrix.append(word)
        for i in range(8-N+1):
            if word[i:N+i] == word[i:N+i][::-1]:
                cnt += 1

    matrix = list(zip(*matrix))
    for j in matrix:
        for i in range(8-N+1):
            if j[i:N+i] == j[i:N+i][::-1]:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))