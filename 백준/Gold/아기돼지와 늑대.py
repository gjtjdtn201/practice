import sys
sys.stdin = open('아기돼지와 늑대.txt')

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

point = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
q = deque()
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 'W':
            q.append((y, x))
            matrix[y][x] == '.'
            visit[y][x] = 1
        elif matrix[y][x] == '.':
            point.append((y, x))

while q:
    a, b = q.popleft()
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        chk = 0
        while matrix[ny][nx] == '+':
            ny += dy[i]
            nx += dx[i]
            if matrix[ny][nx] == '#':
                chk = 1
                ny -= dy[i]
                nx -= dx[i]
                break
        if matrix[ny][nx] == '.' or chk:
            if not visit[ny][nx]:
                q.append((ny, nx))
                visit[ny][nx] = 1
for y, x in point:
    if visit[y][x] == 0:
        matrix[y][x] = 'P'
for i in matrix:
    print("".join(i))

