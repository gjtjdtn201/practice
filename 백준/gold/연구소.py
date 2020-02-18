import sys
sys.stdin = open('연구소.txt', 'r')

from collections import deque
from copy import deepcopy

def virusS(matrix_c, virus_c):
    visit = []
    while virus_c:
        a, b = virus_c.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and matrix_c[ny][nx] == 0 and (ny, nx) not in visit:
                matrix_c[ny][nx] = 2
                virus_c.append((ny, nx))
                visit.append((a, b))

def setwall(st, cnt):
    global maxval

    if cnt == 3:
        matrix2 = deepcopy(matrix)
        virus2 = deepcopy(virus)
        virusS(matrix2,virus2)
        result = 0
        for i in matrix2:
            result += i.count(0)
        if maxval < result:
            maxval = result
        return

    for i in range(st, N*M):
        y = i // M
        x = i % M

        if matrix[y][x] == 0:
            matrix[y][x] = 1
            setwall(i+1, cnt + 1)
            matrix[y][x] = 0

N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

virus = deque()
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 2:
            virus.append((y, x))
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
maxval = 0
setwall(0, 0)
print(maxval)

