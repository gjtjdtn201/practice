import sys
sys.stdin = open('미로 탐색.txt', 'r')

from collections import deque

def BFS(y,x):
    queue = deque()
    queue.append((y,x))
    visit[y][x] = 1
    while queue:
        a, b = queue.popleft()
        if (a, b) == (N-1, M-1):
            print(visit[a][b])
            return
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] != 0 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[a][b] + 1
                queue.append((ny, nx))

N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input())))
dy = [1,-1,0,0]
dx = [0,0,1,-1]
visit = [[0]*M for _ in range(N)]
BFS(0, 0)
