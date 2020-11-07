import sys
sys.stdin = open('마법사 상어와 토네이도.txt')

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 왼 그대로, 오 -dx, 위, 아래 -dy2
dy = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
dx = [0, -1, 0, 1, -2, -1, 0, 1, 0]
dy2 = [-2, -1, -1, 0, 0, 0, 0, 1, 1]
dx2 = [0, -1, 1, -2, -1, 1, 2, -1, 1]
mx = [2, 10, 7, 1, 5, 10, 7, 1, 2]
my = [5, 10, 10, 2, 7, 7, 2, 1, 1]

cnt = 1
point = [0, 0]
delta = -1
i, j = N//2, N//2
ans = 0
chk = 0

while cnt <= N:
    for k in range(cnt):
        j += delta
        if (i, j) == (0, -1):
            chk = 1
            break
        sand = matrix[i][j]
        for move in range(9):
            ny = i - (dy[move] * delta)
            nx = j - (dx[move] * delta)
            part = (matrix[i][j] * mx[move]) // 100
            sand -= part
            if 0 <= ny < N and 0 <= nx < N:
                matrix[ny][nx] += part
            else:
                ans += part
        nx = j + delta
        if 0 <= nx < N:
            matrix[i][nx] += sand
        else:
            ans += sand
        matrix[i][j] = 0
    if chk:
        break
    delta = -delta
    for k in range(cnt):
        i += delta
        sand = matrix[i][j]
        for move in range(9):
            ny = i - (dy2[move] * delta)
            nx = j - (dx2[move] * delta)
            part = (matrix[i][j] * my[move]) // 100
            sand -= part
            if 0 <= ny < N and 0 <= nx < N:
                matrix[ny][nx] += part
            else:
                ans += part
        ny = i + delta
        if 0 <= ny < N:
            matrix[ny][j] += sand
        else:
            ans += sand
        matrix[i][j] = 0
    cnt += 1
print(ans)