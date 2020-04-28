import sys
sys.stdin = open('미세먼지 안녕!.txt')

from collections import deque

R, C, T = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
dust = deque()
for y in range(R):
    for x in range(C):
        if matrix[y][x] == -1:
            cleaner.extend([y, x])
        elif matrix[y][x] > 0:
            dust.append((y, x, matrix[y][x]))
            matrix[y][x] = 0
upy, upx, downy, downx = cleaner
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
tc = 0
while True:
    tc += 1
    while dust:
        a, b, c = dust.popleft()
        d = c//5
        cnt = 0
        stack = []
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] != -1:
                cnt += 1
                stack.append([ny, nx])
        for y, x in stack:
            matrix[y][x] += d
        matrix[a][b] += c-(d*cnt)

    for y in range(upy-1, 0, -1):
        matrix[y][0] = matrix[y-1][0]
    for x in range(C-1):
        matrix[0][x] = matrix[0][x+1]
    for y in range(0, upy):
        matrix[y][C-1] = matrix[y+1][C-1]
    for x in range(C-1, 1, -1):
        matrix[upy][x] = matrix[upy][x-1]
    matrix[upy][1] = 0
    for y in range(downy+1, R-1):
        matrix[y][0] = matrix[y+1][0]
    for x in range(C-1):
        matrix[R-1][x] = matrix[R-1][x+1]
    for y in range(R-1, downy, -1):
        matrix[y][C-1] = matrix[y-1][C-1]
    for x in range(C-1, 0, -1):
        matrix[downy][x] = matrix[downy][x-1]
    matrix[downy][1] = 0
    if tc == T:
        break
    for y in range(R):
        for x in range(C):
            if matrix[y][x] > 0:
                dust.append((y, x, matrix[y][x]))
                matrix[y][x] = 0
ans = 0
for i in matrix:
    ans += sum(i)
print(ans+2)