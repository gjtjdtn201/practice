import sys
sys.stdin = open('빙산.txt', 'r')

from collections import deque
from copy import deepcopy

def chkice(c_matrix):
    cnt = 0
    for y in range(1, N-1):
        for x in range(1, M-1):
            if c_matrix[y][x]:
                cnt += 1
                c_matrix[y][x] = 0
                q.append((y, x))
                qtmp.append((y, x))
                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if c_matrix[ny][nx] != 0:
                            q.append((ny, nx))
                            qtmp.append((ny, nx))
                            c_matrix[ny][nx] = 0
    return cnt

def breakice(c_matrix):
    while qtmp:
        a, b = qtmp.popleft()
        cnt = 0
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if c_matrix[ny][nx] == 0:
                cnt += 1
        if matrix[a][b] - cnt < 0:
            matrix[a][b] = 0
        else:
            matrix[a][b] -= cnt

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q, qtmp = deque(), deque()
chk = ans = 0
while True:
    matrix2 = deepcopy(matrix)
    chk = chkice(matrix2)
    if chk == 0:
        ans = 0
        break
    elif chk > 1:
        break
    matrix2 = deepcopy(matrix)
    breakice(matrix2)
    ans += 1
print(ans)