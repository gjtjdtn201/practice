import sys
sys.stdin = open('구슬 탈출2.txt')

import sys
input = sys.stdin.readline

# BFS 로 풀면 더 쉽당 이건 DFS 코드

def DFS(chk, ry, rx, by, bx, cnt):
    global ans
    # 통과 했다면? 리턴
    if cnt >= ans:
        return
    if chk:
        ans = min(ans, cnt)
        return
    for i in range(4):
        chk4 = 0
        nry, nrx, nby, nbx = ry, rx, by, bx
        while matrix[nry+dy[i]][nrx+dx[i]] != '#' and matrix[nby+dy[i]][nbx+dx[i]] != '#':
            nry += dy[i]
            nrx += dx[i]
            nby += dy[i]
            nbx += dx[i]
            if (nby, nbx) == (hole[0], hole[1]):
                chk4 = 1
            if (nry, nrx) == (hole[0], hole[1]):
                chk = 1
        if chk4:
            chk = 0
            continue
        while matrix[nby+dy[i]][nbx+dx[i]] != '#':
            nby += dy[i]
            nbx += dx[i]
            if (nby, nbx) == (hole[0], hole[1]):
                chk4 = 1
            if (nby, nbx) == (nry, nrx):
                nby -= dy[i]
                nbx -= dx[i]
                break
        if chk4:
            chk = 0
            continue
        while matrix[nry+dy[i]][nrx+dx[i]] != '#':
            nry += dy[i]
            nrx += dx[i]
            if (nry, nrx) == (hole[0], hole[1]):
                chk = 1
            if (nby, nbx) == (nry, nrx):
                nry -= dy[i]
                nrx -= dx[i]
                break
        if (nry, nrx, nby, nbx) == (ry, rx, by, bx):
            continue
        DFS(chk, nry, nrx, nby, nbx, cnt+1)


N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]

# 위, 아래, 왼, 오른
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 11
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 'O':
            hole = [y, x]
        elif matrix[y][x] == 'R':
            red = [y, x]
            matrix[y][x] = '.'
        elif matrix[y][x] == 'B':
            blue = [y, x]
            matrix[y][x] == '.'
DFS(0, red[0], red[1], blue[0], blue[1], 0)
print(-1 if ans == 11 else ans)