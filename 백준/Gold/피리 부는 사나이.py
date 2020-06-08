import sys
sys.stdin = open('피리 부는 사나이.txt')

def DFS(sty, stx, cnt):
    global ans
    stack = [(sty, stx)]
    while stack:
        a, b = stack.pop()
        if matrix[a][b] == 'D':
            ny, nx = a+1, b
        elif matrix[a][b] == 'U':
            ny, nx = a-1, b
        elif matrix[a][b] == 'R':
            ny, nx = a, b+1
        else:
            ny, nx = a, b-1
        if visit[ny][nx] == -1:
            visit[ny][nx] = cnt
            stack.append((ny, nx))
        elif visit[ny][nx] == cnt:
            ans += 1
            return
        else:
            return

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(N)]

visit = [[-1]*M for __ in range(N)]

ans = cnt = 0

for y in range(N):
    for x in range(M):
        if visit[y][x] == -1:
            visit[y][x] = cnt
            DFS(y, x, cnt)
            cnt += 1
print(ans)