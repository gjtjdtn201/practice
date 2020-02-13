import sys
sys.stdin = open('유턴싫어.txt','r')

# 시작 위치
def ST():
    for y in range(R):
        for x in range(C):
            if matrix[y][x] == '.':
                return y, x
# 탐색
def AD(y, x):
    global ans
    # 돌다가 갈곳 잃으면 1 반환하고 끝
    atmp = 0
    visited.append((y, x))
    for i in range(4):
        ny = y + direction[i][0]
        nx = x + direction[i][1]
        if safe(ny, nx):
            atmp += 1
    if atmp == 1:
        ans = 1
        return
    for i in range(4):
        ny = y + direction[i][0]
        nx = x + direction[i][1]
        if safe(ny, nx) and (ny, nx) not in visited:
            AD(ny, nx)

def safe(y, x):
    return R > y >= 0 and C > x >= 0 and (matrix[y][x] == '.' or matrix[y][x] == 2)

R, C = map(int, input().split())
matrix = []
for i in range(R):
    matrix.append(list(input()))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
atmp = 0

# 시작점 좌표 반환
sty, stx = ST()
visited = []
AD(sty, stx)

print(ans)