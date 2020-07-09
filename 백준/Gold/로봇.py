import sys
sys.stdin = open('로봇.txt')

from collections import deque

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(M)]

sty, stx, stdir = map(int, input().split())
edy, edx, eddir = map(int, input().split())
# 동 서 남 북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visit = [[[-1]*4 for _ in range(N)] for __ in range(M)]

q = deque()
q.append((sty-1, stx-1, stdir-1))
visit[sty-1][stx-1][stdir-1] = 0
while q:
    a, b, c = q.popleft()
    if (a, b, c) == (edy-1, edx-1, eddir-1):
        print(visit[a][b][c])
        break
    if c > 1:
        if visit[a][b][0] == -1:
            q.append((a, b, 0))
            visit[a][b][0] = visit[a][b][c] + 1
        if visit[a][b][1] == -1:
            q.append((a, b, 1))
            visit[a][b][1] = visit[a][b][c] + 1
    else:
        if visit[a][b][2] == -1:
            q.append((a, b, 2))
            visit[a][b][2] = visit[a][b][c] + 1
        if visit[a][b][3] == -1:
            q.append((a, b, 3))
            visit[a][b][3] = visit[a][b][c] + 1
    for i in range(1, 4):
        ny = a + dy[c]*i
        nx = b + dx[c]*i
        if 0 <= ny < M and 0 <= nx < N:
            if matrix[ny][nx] == 1:
                break
            if visit[ny][nx][c] == -1 or visit[ny][nx][c] > visit[a][b][c] + 1:
                q.append((ny, nx, c))
                visit[ny][nx][c] = visit[a][b][c] + 1