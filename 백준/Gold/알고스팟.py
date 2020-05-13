import sys
sys.stdin = open('알고스팟.txt')

from collections import deque

def BFS():
    q = deque()
    q.append((0, 0))
    visit[0][0] = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == -1:
                if matrix[ny][nx] == 0:
                    if (ny, nx) == (N-1, M-1):
                        print(visit[a][b])
                        return
                    q.appendleft((ny, nx))
                    visit[ny][nx] = visit[a][b]
                else:
                    q.append((ny, nx))
                    visit[ny][nx] = visit[a][b] + 1

M, N = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]

visit = [[-1]*M for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
print(0) if (M, N) == (1, 1) else BFS()
