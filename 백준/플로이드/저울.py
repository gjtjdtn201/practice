import sys
sys.stdin = open('저울.txt')

N = int(input())
M = int(input())

matrix = [[0]*N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] + matrix[k][j] == 2:
                matrix[i][j] = 1

for y in range(N):
    cnt = 0
    for x in range(N):
        if matrix[y][x] + matrix[x][y] == 0:
            cnt += 1
    print(cnt-1)