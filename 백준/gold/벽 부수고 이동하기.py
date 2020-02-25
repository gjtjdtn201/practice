import sys
sys.stdin = open('벽 부수고 이동하기.txt', 'r')

from collections import deque

def BFS():
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        a, b, c = queue.popleft()
        if (a, b) == (N - 1, M - 1):
            return visited[a][b][c]
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][c]:
                if matrix[ny][nx] == 0:
                    visited[ny][nx][c] = visited[a][b][c] + 1
                    queue.append((ny, nx, c))
                elif matrix[ny][nx] == 1 and c == 0:
                    visited[ny][nx][1] = visited[a][b][c] + 1
                    queue.append((ny, nx, 1))
    return -1


N, M = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for __ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque()

print(BFS())