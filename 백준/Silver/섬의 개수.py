import sys
sys.stdin = open('섬의 개수.txt')

from collections import deque

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0 , 1, 1, 1, 0, -1, -1]

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    chk = 2
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 1:
                q = deque()
                q.append((y, x))
                visit[y][x] = 1
                while q:
                    a, b = q.popleft()
                    for i in range(8):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0:
                            if matrix[ny][nx] == 1:
                                matrix[ny][nx] = chk
                                q.append((ny, nx))
                                visit[ny][nx] = 1
                chk += 1
    print(chk-2)