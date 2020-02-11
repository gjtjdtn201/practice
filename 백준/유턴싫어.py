import sys
sys.stdin = open('유턴싫어.txt','r')

# 시작 위치
def ST():
    for y in range(R):
        for x in range(C):
            if matrix[y][x] == '.':
                return y, x
# 탐색
def AD(y,x):
    visit.append((y,x))
    matrix[y][x] = 'X'
    chk = 0
    for i in range(4):
        chk += 1
        ny = y + direction[chk][0]
        nx = x + direction[chk][1]
        if safe(ny,nx) and (y,x) not in visit:
            AD(ny,nx)

def safe(y,x):
    return R > y >= 0 and C > x >= 0 and matrix[y][x] == '.'

R, C = map(int, input().split())
matrix = []
for i in range(R):
    matrix.append(list(input()))

direction = [(1,0),(-1,0),(0,1),(0,-1)]
chk = 0
visit = []
sty, stx = ST()
AD(sty,stx)
for i in matrix:
    print(i)