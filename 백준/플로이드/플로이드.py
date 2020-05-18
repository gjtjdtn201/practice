import sys
sys.stdin = open('플로이드.txt')

N = int(input())
M = int(input())

matrix = [[float('inf')]*N for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = min(matrix[a-1][b-1], c)
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                matrix[j][k] = 0
            else:
                matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
for y in range(N):
    for x in range(N):
        print(0 if matrix[y][x] == float('inf') else matrix[y][x], end=' ')
    print()