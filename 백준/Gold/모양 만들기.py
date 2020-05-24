import sys
sys.stdin = open('모양 만들기.txt')

from collections import deque

def BFS(sty, stx, chk):
    q = deque()
    q.append((sty, stx))
    matrix[sty][stx] = chk
    cnt = 0
    while q:
        a, b = q.popleft()
        cnt += 1
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 1:
                q.append((ny, nx))
                matrix[ny][nx] = chk
    return cnt


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

color = [0, 0]
chk = 1
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            chk += 1
            matrix[y][x] = chk
            color.append(BFS(y, x, chk))
ans = 0
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 0:
            chk, cnt = [], 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if matrix[ny][nx] not in chk:
                        chk.append(matrix[ny][nx])
            for i in chk:
                cnt += color[i]
            ans = max(ans, cnt)
print(ans)