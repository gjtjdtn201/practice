def SP(x, y, shape):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return

    if shape == 1:
        if y+1 < N and matrix[x][y+1] == 0:
            SP(x, y+1, 1)

        if x+1 < N and y+1 < N and matrix[x][y+1] == 0 and matrix[x+1][y] == 0 and matrix[x+1][y+1] == 0:
            SP(x+1, y+1, 3)
    elif shape == 2:
        if x + 1 < N and matrix[x+1][y] == 0:
            SP(x+1, y, 2)

        if x + 1 < N and y + 1 < N and matrix[x][y + 1] == 0 and matrix[x + 1][y] == 0 and matrix[x + 1][y + 1] == 0:
            SP(x + 1, y + 1, 3)
    else:
        if y + 1 < N and matrix[x][y + 1] == 0:
            SP(x, y + 1, 1)

        if x + 1 < N and matrix[x+1][y] == 0:
            SP(x+1, y, 2)

        if x + 1 < N and y + 1 < N and matrix[x][y + 1] == 0 and matrix[x + 1][y] == 0 and matrix[x + 1][y + 1] == 0:
            SP(x + 1, y + 1, 3)


N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

cnt = 0
SP(0, 1, 1)
print(cnt)