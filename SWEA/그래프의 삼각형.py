import sys
sys.stdin = open('그래프의 삼각형.txt', 'r')

T = int(input())

for test_case in range(1, T + 1) :
    N, M = map(int, input().split())
    matrix = [[] for num in range(N)]
    for i in range(M) :
        x, y = map(int, input().split())
        matrix[x - 1].append(y - 1)
    cnt = 0
    for i in range(N - 2) :
        for j in matrix[i] :
            for k in matrix[j] :
                if k in matrix[i] :
                    cnt += 1

    print('#{} {}'.format(test_case, cnt))