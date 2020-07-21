import sys
sys.stdin = open('직사각형 탈출.txt')

from collections import deque

def BFS():
    while q:
        a, b = q.popleft()
        for i in range(4):
            chk = 0
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and matrix[ny][nx] == 0:
                if i == 0 and ny+(H-1) < N:
                    for j in range(W):
                        mx = nx + j
                        if mx >= M or matrix[ny+(H-1)][mx] == 1:
                            chk = 1
                            break

                elif i == 1:
                    for j in range(W):
                        mx = nx + j
                        if mx >= M or matrix[ny][mx] == 1:
                            chk = 1
                            break

                elif i == 2 and nx+(W-1) < M:
                    for j in range(H):
                        my = ny + j
                        if my >= N or matrix[my][nx+(W-1)] == 1:
                            chk = 1
                            break

                else:
                    for j in range(W):
                        my = ny + j
                        if my >= N or matrix[my][nx] == 1:
                            chk = 1
                            break
                if chk:
                    continue
                if (ny, nx) == (edy-1, edx-1):
                    print(visit[a][b])
                    return
                q.append((ny, nx))
                visit[ny][nx] = visit[a][b] + 1
    print(-1)

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

H, W, sty, stx, edy, edx = map(int, input().split())

q = deque()
q.append((sty-1, stx-1))

# 아래, 위, 오른, 왼
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

visit = [[0]*M for _ in range(N)]
visit[sty-1][stx-1] = 1
if (sty, stx) == (edy, edx):
    print(0)
else:
    BFS()
    