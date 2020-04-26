import sys
sys.stdin = open('거울 설치.txt')

from collections import deque
import sys
input = sys.stdin.readline

def move(y, x):
    if 0 <= y < N and 0 <= x < N and matrix[y][x] != 1:
        return True
    return False

def bfs():
    while q:
        a, b, c = q.popleft()
        if (a, b) == (edy, edx):
            print(dist[a][b][c])
            return
        ny = a + dy[c]
        nx = b + dx[c]
        while move(ny, nx) and matrix[ny][nx] == 0:
            ny += dy[c]
            nx += dx[c]
        if move(ny, nx) and matrix[ny][nx] == 2:
            dist[ny][nx][c] = dist[a][b][c]
            q.append((ny, nx, c))
            k = 2 if c < 2 else 0
            for i in range(k, k+2):
                if dist[ny][nx][i] == -1:
                    dist[ny][nx][i] = dist[a][b][c]+1
                    q.append((ny, nx, i))

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
dist = [[[-1]*4 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
door = []
for y in range(N):
    for x in range(N):
        if matrix[y][x] == '#':
            door.extend([y, x])
            matrix[y][x] = 2
        elif matrix[y][x] == '*':
            matrix[y][x] = 1
        elif matrix[y][x] == '!':
            matrix[y][x] = 2
        else:
            matrix[y][x] = 0

sty, stx, edy, edx = door
for i in range(4):
    ny = sty + dy[i]
    nx = stx + dx[i]
    if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] != 1:
        q.append((sty, stx, i))
        dist[sty][stx][i] = 0
bfs()