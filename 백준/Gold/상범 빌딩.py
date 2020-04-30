import sys
sys.stdin = open('상범 빌딩.txt')

import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    while q:
        c, a, b = q.popleft()
        for i in range(6):
            nz = c + dz[i]
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                if matrix[nz][ny][nx] == 0 and not visit[nz][ny][nx]:
                    if (nz, ny, nx) == (edz, edy, edx):
                        print('Escaped in {} minute(s).'.format(visit[c][a][b]))
                        return
                    q.append((nz, ny, nx))
                    visit[nz][ny][nx] = visit[c][a][b] + 1
    print('Trapped!')

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    matrix = [[] for _ in range(L)]
    visit = [[[0]*C for _ in range(R)] for __ in range(L)]
    for tc in range(L):
        for _ in range(R):
            matrix[tc].append(list(input().rstrip()))
        input()
    q = deque()
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if matrix[z][y][x] == 'S':
                    q.append((z, y, x))
                    visit[z][y][x] = 1
                    matrix[z][y][x] = 0
                elif matrix[z][y][x] == 'E':
                    edz, edy, edx = z, y, x
                    matrix[z][y][x] = 0
                elif matrix[z][y][x] == '.':
                    matrix[z][y][x] = 0
                else:
                    matrix[z][y][x] = 1
    BFS()