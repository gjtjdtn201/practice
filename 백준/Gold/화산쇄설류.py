import sys
sys.stdin = open('화산쇄설류.txt')

from collections import deque

M, N, V = map(int, input().split())

X, Y = map(int, input().split())
sty, stx = X-1, Y-1
matrix = [list(map(int, input().split())) for _ in range(M)]
vol = deque()
visit = [[-1]*N for __ in range(M)]
vol_v = [[float('inf')]*N for __ in range(M)]
for i in range(V):
    x, y, t = map(int, input().split())
    vol.append((x-1, y-1, t))
    vol_v[x-1][y-1] = t
    visit[x-1][y-1] = -2

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque()
q.append((sty, stx))
visit[sty][stx] = 0

ans = [matrix[sty][stx], 0]

while vol:
    a, b, c = vol.popleft()
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < M and 0 <= nx < N and vol_v[ny][nx] > c+1:
            vol.append((ny, nx, c+1))
            vol_v[ny][nx] = c+1
while q:
    a, b = q.popleft()
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < M and 0 <= nx < N and visit[ny][nx] == -1 and vol_v[ny][nx] > visit[a][b]+1:
            q.append((ny, nx))
            visit[ny][nx] = visit[a][b] + 1
            if ans[0] < matrix[ny][nx]:
                ans = [matrix[ny][nx], visit[ny][nx]]

print(*ans)