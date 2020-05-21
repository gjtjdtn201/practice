import sys
sys.stdin = open('불!.txt')

import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    while q:
        a, b, c = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                if c == 1:
                    continue
                print(visit[a][b])
                return
            if matrix[ny][nx] == '.' and visit[ny][nx] == 0:
                q.append((ny, nx, c))
                visit[ny][nx] = visit[a][b] + 1

    print('IMPOSSIBLE')
    return

R, C = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(R)]
visit = [[0]*C for _ in range(R)]

q = deque()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for y in range(R):
    for x in range(C):
        if matrix[y][x] == 'J':
            q.append((y, x, 0))
            matrix[y][x] = '.'
            visit[y][x] = 1
        elif matrix[y][x] == 'F':
            q.appendleft((y, x, 1))
            visit[y][x] = 1
BFS()