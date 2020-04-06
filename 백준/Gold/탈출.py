import sys
sys.stdin = open('탈출.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline


def water():
    while wq:
        a, b = wq.popleft()
        if matrix[a][b] == '.':
            matrix[a][b] = '*'
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not wv[ny][nx] and matrix[ny][nx] == '.':
                wqtmp.append((ny, nx))
                wv[ny][nx] = 1


R, C = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(R)]

queue, qtmp, wq, wqtmp = deque(), deque(), deque(), deque()

visit = [[0]*C for _ in range(R)]
wv = [[0]*C for _ in range(R)]

for y in range(R):
    for x in range(C):
        if matrix[y][x] == 'D':
            edy, edx = y, x
        elif matrix[y][x] == 'S':
            sty, stx = y, x
        elif matrix[y][x] == '*':
            wq.append((y, x))
            wv[y][x] = 1

queue.append((sty, stx))
visit[sty][stx] = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
end = 0
water()
wq = wqtmp
wqtmp = deque()
while not end:
    water()
    while queue:
        a, b = queue.popleft()
        if (a, b) == (edy, edx):
            end = 1
            print(visit[a][b]-1)
            break
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and (matrix[ny][nx] == '.' or matrix[ny][nx] == 'D'):
                qtmp.append((ny, nx))
                visit[ny][nx] = visit[a][b] + 1
    else:
        if not qtmp:
            end = 1
            print('KAKTUS')
        else:
            queue, wq = qtmp, wqtmp
            qtmp, wqtmp = deque(), deque()