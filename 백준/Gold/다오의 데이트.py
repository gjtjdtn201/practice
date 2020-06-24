import sys
sys.stdin = open('다오의 데이트.txt')

def DFS(y, x, cnt, chk):
    global ans, move
    if (y, x) == (edy, edx):
        ans = 'YES'
        move = chk
        return
    if cnt >= N:
        return
    for i in force[cnt]:
        ny = y + dy[dist[i]]
        nx = x + dx[dist[i]]
        if 0 <= ny < H and 0 <= nx < W and matrix[ny][nx] != '@':
            DFS(ny, nx, cnt+1, chk+i)

H, W = map(int, input().split())

matrix = [list(input()) for _ in range(H)]

N = int(input())
force = []
for i in range(N):
    force.append(input().split())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
dist = {'W': 1, 'A': 3, 'S': 0, 'D': 2}

for y in range(H):
    for x in range(W):
        if matrix[y][x] == 'D':
            sty, stx = y, x
            matrix[y][x] = '.'
        elif matrix[y][x] == 'Z':
            edy, edx = y, x
ans = 'NO'
move = ''
DFS(sty, stx, 0, move)
print(ans)
if move != '':
    print(move)