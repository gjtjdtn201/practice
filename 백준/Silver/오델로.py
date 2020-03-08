import sys
sys.stdin = open('오델로.txt', 'r')

import sys
input = sys.stdin.readline
from collections import deque

def CC(y, x):
    for i in range(8):
        tmp = []
        for j in range(1, 6):
            ny = y + dy[i]*j
            nx = x + dx[i]*j
            if 0 <= ny < 6 and 0 <= nx < 6:
                if matrix[ny][nx] == chk[1]:
                    tmp.append((ny, nx))
                elif matrix[ny][nx] == chk[0]:
                    while tmp:
                        a, b = tmp.pop()
                        matrix[a][b] = chk[0]
                    break
                else:
                    break

matrix = [['.']*6 for _ in range(6)]

matrix[2][2] = 'W'
matrix[3][3] = 'W'
matrix[2][3] = 'B'
matrix[3][2] = 'B'

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N = int(input())
chk = deque()
chk.extend(['B','W'])
for i in range(N):
    R, C = map(int, input().split())
    matrix[R-1][C-1] = chk[0]
    CC(R-1, C-1)
    chk.rotate(-1)
cnt = cnt2 = 0
for i in matrix:
    cnt += i.count('W')
    cnt2 += i.count('B')
    print(''.join(i))
if cnt > cnt2:
    print('White')
else:
    print('Black')