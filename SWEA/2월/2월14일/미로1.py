import sys
sys.stdin = open('미로1.txt', 'r')

def ST():
    for y in range(16):
        for x in range(16):
            if matrix[y][x] == 2:
                return y, x

def DFS(y, x):
    global ans
    stack = [(y, x)]
    visit = []
    while stack:
        a, b = stack.pop()
        visit.append((a, b))
        if matrix[a][b] == 3:
            ans = 1
            return
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < 16 and 0 <= nx < 16 and (matrix[ny][nx] == 0 or matrix[ny][nx] == 3) and (ny, nx) not in visit:
                stack.append((ny, nx))

for test_case in range(1, 11):
    T = int(input())
    matrix = []
    for i in range(16):
        matrix.append(list(map(int, input())))

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    sty, stx = ST()
    ans = 0
    DFS(sty, stx)
    print('#{} {}'.format(test_case, ans))