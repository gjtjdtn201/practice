import sys
sys.stdin = open('치즈2.txt', 'r')

from collections import deque

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans = -1
q = deque()

while True:
    ans += 1
    cnt = 0
    q.append((0, 0))
    matrix[0][0] = -1
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] > 0:
                    matrix[ny][nx] += 1
                    cnt += 1
                elif matrix[ny][nx] == 0:
                    matrix[ny][nx] = -1
                    q.append((ny, nx))
    if cnt == 0:
        break
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == -1:
                matrix[y][x] = 0
            elif matrix[y][x] > 2:
                matrix[y][x] = 0
            elif matrix[y][x] == 2:
                matrix[y][x] = 1
print(ans)