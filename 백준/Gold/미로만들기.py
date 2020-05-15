import sys
sys.stdin = open('미로만들기.txt', 'r')

from collections import deque

def BFS():
    q = deque()
    q.append((0, 0, 0))
    visit[0][0] = 0
    while q:
        a, b, c = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == -1:
                if (ny, nx) == (N-1, N-1):
                    return c
                if matrix[ny][nx]:
                    visit[ny][nx] = c
                    q.appendleft((ny, nx, c))
                else:
                    visit[ny][nx] = c+1
                    q.append((ny, nx, c+1))
    return 0

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visit = [[-1]*N for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
print(BFS())