import sys
sys.stdin = open('움직이는 미로 탈출.txt')

from collections import deque

matrix = [list(input()) for _ in range(8)]

dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1, 0]

q = deque()
q.append((7, 0))
while q:
    a, b = q.popleft()
    for i in range(9):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < 8 and 0 <= nx < 8:
            if ny != 0 and matrix[ny-1][nx] == '.':
                q.append((ny, nx))
            elif ny == 0:
                q.append((ny, nx))