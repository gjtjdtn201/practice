import sys
sys.stdin = open('숫자 배열 회전.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    ans = [[0 for y in range(3)] for x in range(N)]
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    for z in range(3):
        matrix = list(zip(*matrix[::-1]))
        for i in range(N):
            cnt = ''
            for j in range(N):
                cnt += str(matrix[i][j])
            ans[i][z] = cnt
    print('#{}'.format(test_case))
    for i in ans:
        print(*tuple(i))