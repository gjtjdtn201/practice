import sys
sys.stdin = open('드래곤 커브.txt', 'r')

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def curve():
    global y, x
    for i in range(len(stack)-1, -1, -1):
        z = 0 if stack[i] + 1 > 3 else stack[i] + 1
        y += dy[z]
        x += dx[z]
        matrix[y][x] = 1
        stack.append(z)

N = int(input())
matrix = [[0]*101 for _ in range(101)]
for __ in range(N):
    x, y, d, g = map(int, input().split())
    matrix[y][x] = 1
    y += dy[d]
    x += dx[d]
    matrix[y][x] = 1
    stack = [d]
    for i in range(g):
        curve()
ans = 0
for a in range(100):
    for b in range(100):
        if matrix[a][b] == 1 and matrix[a+1][b] == 1 and matrix[a][b+1] == 1 and matrix[a+1][b+1] == 1:
            ans += 1
print(ans)