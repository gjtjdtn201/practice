import sys
sys.stdin = open('회장뽑기.txt')

N = int(input())
matrix = [[float('inf')]*N for _ in range(N)]

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
ans2 = float('inf')
for y in range(N):
    cnt = 0
    for x in range(N):
        cnt = max(cnt, matrix[y][x])
    if ans2 > cnt:
        ans = [y+1]
        ans2 = cnt
    elif ans2 == cnt:
        ans.append(y+1)
print(ans2, len(ans))
print(*ans)