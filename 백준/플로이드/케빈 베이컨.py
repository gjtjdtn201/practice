import sys
sys.stdin = open('케빈 베이컨.txt')

N, M = map(int, input().split())
matrix = [[float('inf')]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1], matrix[b-1][a-1] = 1, 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
cnt, ans = float('inf'), 0
for i in range(N):
    n = sum(matrix[i])
    if cnt > n:
        cnt = n
        ans = i+1
print(ans)