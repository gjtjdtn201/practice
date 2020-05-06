import sys
sys.stdin = open('뿌요뿌요.txt')

import sys
input = sys.stdin.readline

from collections import deque

def BFS(y, x, R):
    global chk
    q = deque()
    q.append((y, x))
    visit = [(y, x)]
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < 12 and 0 <= nx < 6 and (ny, nx) not in visit:
                if matrix[ny][nx] == R:
                    q.append((ny, nx))
                    visit.append((ny, nx))
    if len(visit) >= 4:
        chk = 0
        for i, j in visit:
            matrix[i][j] = '.'

matrix = [list(input().rstrip()) for _ in range(12)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ans = 0
while True:
    chk = 1
    for y in range(12):
        for x in range(6):
            if matrix[y][x] != '.':
                BFS(y, x, matrix[y][x])
    if chk:
        print(ans)
        break
    ans += 1
    for i in range(6):
        stack = []
        for j in range(12):
            if matrix[j][i] != '.':
                stack.append(matrix[j][i])
        idx = 11
        while stack:
            matrix[idx][i] = stack.pop()
            idx -= 1
        while idx >= 0:
            matrix[idx][i] = '.'
            idx -= 1
