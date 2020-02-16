import sys
sys.stdin = open('안전 영역.txt', 'r')

from collections import deque
from copy import deepcopy

def SS(i):
    for y in range(N):
        for x in range(N):
            if matrix1[y][x] > i:
                return y, x


def BSF(y, x, val):
    queue = deque()
    queue.append((y,x))
    matrix1[y][x] = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and matrix1[ny][nx] > val:
                queue.append((ny, nx))
                matrix1[ny][nx] = 0

N = int(input())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

dy = [1,-1,0,0]
dx = [0,0,1,-1]

maxv = 0
cnt = 0
for i in matrix:
    k = max(i)
    if cnt < k:
        cnt = k

for i in range(cnt):
    matrix1 = deepcopy(matrix)
    chk = 0
    while SS(i):
        sty, stx = SS(i)
        BSF(sty, stx, i)
        chk += 1
    if maxv < chk:
        maxv = chk

print(maxv)