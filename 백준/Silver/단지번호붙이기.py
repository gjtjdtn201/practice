import sys
sys.stdin = open('단지번호붙이기.txt', 'r')

def DG():
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 1:
                return y, x
    return False

def DFS(y, x):
    stack = [(y, x)]
    matrix[y][x] = 0
    cnt = 1
    while stack:
        a, b = stack.pop()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 1:
                stack.append((ny, nx))
                matrix[ny][nx] = 0
                cnt += 1
    return cnt

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input())))

dy = [1,-1,0,0]
dx = [0,0,1,-1]

ans = []

while DG():
    sty, stx = DG()
    ans.append(DFS(sty, stx))
ans.sort()
print(len(ans))
for i in ans:
    print(i)