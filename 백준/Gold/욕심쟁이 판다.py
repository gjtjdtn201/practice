import sys
sys.stdin = open('욕심쟁이 판다.txt')

def dp(a, b):
    visit[a][b] = 1
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if matrix[a][b] < matrix[ny][nx]:
                if visit[ny][nx]:
                    visit[a][b] = max(visit[a][b], visit[ny][nx]+1)
                else:
                    visit[a][b] = max(visit[a][b], dp(ny, nx)+1)
    return visit[a][b]

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ans = 0
for y in range(N):
    for x in range(N):
        ans = max(ans, dp(y, x))
print(ans)