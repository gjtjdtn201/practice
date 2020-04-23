import sys
sys.stdin = open('견우와 직녀.txt')

from collections import deque

def BFS():
    while q:
        a, b, c, d = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx][c]:
                if (ny, nx) == (N-1, N-1):
                    print(d)
                    return
                if matrix[ny][nx] == 0 and c == 0 and matrix[a][b] == 1:
                    if d%M == 0:
                        q.append((ny, nx, 1, d+1))
                        visit[ny][nx][1] = d+1
                    else:
                        q.append((a, b, 0, d+1))
                elif matrix[ny][nx] == 1:
                    q.append((ny, nx, c, d+1))
                    visit[ny][nx][c] = d+1
                elif matrix[ny][nx] > 1 and matrix[a][b] == 1:
                    if d%matrix[ny][nx] == 0:
                        visit[ny][nx][c] = d+1
                        q.append((ny, nx, c, d+1))
                    else:
                        q.append((a, b, c, d+1))

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[[0, 0] for _ in range(N)] for __ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 0:
            chk, chk1 = 0, 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 0:
                    if i == 0 or i == 1:
                        chk = 1
                    elif i == 2 or i == 3:
                        chk1 = 1
            if (chk, chk1) == (1, 1):
                matrix[y][x] = -1

q = deque()
q.append((0, 0, 0, 1))
visit[0][0][0] = 1

BFS()