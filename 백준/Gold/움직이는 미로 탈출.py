import sys
sys.stdin = open('움직이는 미로 탈출.txt')

from collections import deque

matrix = deque(list(input()) for _ in range(8))
wall = []
for y in range(8):
    for x in range(8):
        if matrix[y][x] == '#':
            wall.append((y, x))
if wall:
    dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1, 0]

    q = deque()
    q.append((7, 0))
    for i in range(8):
        qtmp = deque()
        chk = 1
        while q:
            a, b = q.popleft()
            for i in range(9):
                ny = a + dy[i]
                nx = b + dx[i]
                if 0 <= ny < 8 and 0 <= nx < 8 and matrix[ny][nx] == '.':
                    if ny != 0 and matrix[ny-1][nx] == '.':
                        qtmp.append((ny, nx))
                        chk = 0
                    elif ny == 0:
                        qtmp.append((ny, nx))
                        chk = 0
        if chk:
            print(0)
            break
        q = qtmp
        matrix.pop()
        matrix.appendleft(['.']*8)
    else:
        print(1)
else:
    print(1)