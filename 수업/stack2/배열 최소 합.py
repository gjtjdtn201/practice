import sys
sys.stdin = open("배열 최소 합.txt", "r")

from itertools import permutations

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    HB = permutations(range(N))
    ans = 9999
    for y in HB:
        cnt = 0
        for k in range(N):
            cnt += matrix[y[k]][k]
            if cnt > ans:
                break
        if cnt < ans:
            ans = cnt
    print('#{} {}'.format(test_case, ans))