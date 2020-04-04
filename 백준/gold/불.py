import sys
sys.stdin = open('불.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline

def ST():
    global chk
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == '@':
                matrix[y][x] = '.'
                sty, stx = y, x
            elif matrix[y][x] == '*':
                q.append((y, x, 1))
                visit[y][x] = 1
    return sty, stx

def BFS():
    q.append((sty, stx, 0))
    visit[sty][stx] = 1
    while q:
        a, b, c = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                if c == 1:
                    continue
                print(visit[a][b])
                return
            if visit[ny][nx] or matrix[ny][nx] == '#':
                continue
            visit[ny][nx] = visit[a][b] + 1
            q.append((ny, nx, c))
    print('IMPOSSIBLE')

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for tc in range(int(input())):
    w, h = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(h)]
    q = deque()
    visit = [[0]*w for _ in range(h)]
    sty, stx = ST()
    BFS()