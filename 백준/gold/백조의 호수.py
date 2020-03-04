import sys
sys.stdin = open('백조의 호수.txt', 'r')

def chkice():
    while wq:
        a, b = wq.popleft()
        if matrix[a][b] == 'X':
            matrix[a][b] = '.'
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not icev[ny][nx]:
                if matrix[ny][nx] == 'X':
                    wqtmp.append((ny, nx))
                else:
                    wq.append((ny, nx))
                icev[ny][nx] = 1

import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(R)]
icev = [[0] * C for __ in range(R)]
visit = [[0] * C for ___ in range(R)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
swan = []
wq, wqtmp, q, qtmp = deque(), deque(), deque(), deque()
cnt = 0
for y in range(R):
    for x in range(C):
        if matrix[y][x] == 'L':
            swan.extend((y, x))
            wq.append((y, x))
            matrix[y][x] = '.'
        elif matrix[y][x] == '.':
            icev[y][x] = 1
            wq.append((y, x))
sty, stx, edy, edx = swan
q.append((sty, stx))
visit[sty][stx] = 1
chk = ans = 0
while chk == 0:
    chkice()
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not visit[ny][nx]:
                if matrix[ny][nx] == '.':
                    if (ny, nx) == (edy, edx):
                        chk = 1
                        break
                    q.append((ny, nx))
                else:
                    qtmp.append((ny, nx))
                visit[ny][nx] = 1
        if chk == 1:
            break
    if chk == 0:
        ans += 1
        q, wq = qtmp, wqtmp
        qtmp, wqtmp = deque(), deque()

print(ans)