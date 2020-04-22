import sys
sys.stdin = open('견우와 직녀.txt')

from collections import deque

def BFS():
    while q:
        a, b, c = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx][c]:
                if (ny, nx) == (N-1, N-1):
                    print(visit[a][b][c])
                    return
                if matrix[ny][nx] == 0 and c == 0:
                    q.append((ny, nx, 1))
                    if visit[a][b][c] % M == 0:
                        visit[ny][nx][1] = visit[a][b][c] + 1
                    else:
                        visit[ny][nx][1] = visit[a][b][c] + 1 + (M - (visit[a][b][c] % M))
                elif matrix[ny][nx] == 1:
                    q.append((ny, nx, c))
                    visit[ny][nx][c] = visit[a][b][c]+1
                elif matrix[ny][nx] > 1 and c == 0:
                    q.append((ny, nx, 1))
                    if visit[a][b][c]%matrix[ny][nx] == 0:
                        visit[ny][nx][1] = visit[a][b][c]+1
                    else:
                        visit[ny][nx][1] = visit[a][b][c]+1+(matrix[ny][nx]-(visit[a][b][c]%matrix[ny][nx]))


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[[0, 0] for _ in range(N)] for __ in range(N)]

q = deque()
q.append((0, 0, 0))
visit[0][0][0] = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

BFS()
for i in visit:
    print(i)