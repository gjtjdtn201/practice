import sys
sys.stdin = open('케빈 베이컨.txt')

N, M = map(int, input().split())
matrix = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k]+matrix[k][j] == 2 or matrix[i][j] == 1:
                matrix[i][j] = 1
ans = 0
for y in range(N):
    cnt = 0
    for x in range(N):
        cnt += matrix[y][x] + matrix[x][y]
    if cnt == N-1:
        ans += 1
print(ans)