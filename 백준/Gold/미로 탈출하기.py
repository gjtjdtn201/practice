import sys
sys.stdin = open('미로 탈출하기.txt')

import sys
input = sys.stdin.readline

def DFS(sty, stx, color):
    global cnt
    stack = [(sty, stx)]
    visit[sty][stx] = color
    moves = 0
    while stack:
        a, b = stack.pop()
        moves += 1
        dy, dx = move[matrix[a][b]]
        ny = a + dy
        nx = b + dx
        if 0 > ny or N <= ny or 0 > nx or M <= nx:
            cnt += moves
            return True
        if visit[ny][nx] == 0:
            visit[ny][nx] = color
            stack.append((ny, nx))
            continue
        if colors[visit[ny][nx]] == 1:
            cnt += moves
            return True
        return False


N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

move = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

visit = [[0]*M for _ in range(N)]

cnt = 0
chk = 1
colors = {}

for y in range(N):
    for x in range(M):
        if visit[y][x] == 0:
            colors[chk] = 0
            if DFS(y, x, chk):
                colors[chk] = 1
            chk += 1

print(cnt)