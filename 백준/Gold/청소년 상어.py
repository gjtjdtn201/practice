import sys
sys.stdin = open('청소년 상어.txt')

from copy import deepcopy

def DFS(y, x, cnt, dist):
    global ans, matrix, fish
    move(y, x)

    while True:
        ny = y + dy[dist]
        nx = x + dx[dist]
        y, x = ny, nx
        if not 0 <= ny < 4 or not 0 <= nx < 4:
            ans = max(ans, cnt)
            return
        if not matrix[ny][nx]:
            continue
        c_matrix, c_fish = deepcopy(matrix), deepcopy(fish)
        tmp = matrix[ny][nx]
        fish[tmp[0]], matrix[ny][nx] = [], []
        DFS(ny, nx, cnt+tmp[0]+1, tmp[1])
        matrix, fish = c_matrix, c_fish

def move(sy, sx):
    for i in range(16):
        if fish[i]:
            y, x = fish[i]
            for j in range(8):
                chk = matrix[y][x][1] + j
                if chk > 7:
                    chk -= 8
                ny = y + dy[chk]
                nx = x + dx[chk]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if (ny, nx) == (sy, sx):
                        continue
                    if matrix[ny][nx]:
                        fish[matrix[ny][nx][0]] = [y, x]
                    fish[i] = [ny, nx]
                    matrix[ny][nx], matrix[y][x] = [matrix[y][x][0], chk], matrix[ny][nx]
                    break

matrix = [[] for _ in range(4)]
fish = [[] for _ in range(16)]
for i in range(4):
    A = list(map(int, input().split()))
    for j in range(4):
        matrix[i].append([A[j*2]-1, A[j*2+1]-1])
        fish[A[j*2]-1] = [i, j]

# 상어가 처음 위치에 들어감
cnt, dist = matrix[0][0][0]+1, matrix[0][0][1]
fish[matrix[0][0][0]] = []
matrix[0][0] = []

# 0번이 위 반시계 방향으로 7까지 증가
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0

DFS(0, 0, cnt, dist)
print(ans)