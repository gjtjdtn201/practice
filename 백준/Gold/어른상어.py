import sys
sys.stdin = open('어른상어.txt')

N, M, k = map(int, input().split())

start = [list(map(int, input().split())) for _ in range(N)]
matrix = [[[-1, -1] for _ in range(N)] for __ in range(N)]

# 1234 위 아래 왼쪽 오른쪽
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

first = list(map(int, input().split()))
sharks_dir = [[[] for _ in range(4)] for __ in range(M)]

for i in range(M):
    for j in range(4):
        a, b, c, d = map(int, input().split())
        sharks_dir[i][j] = [a-1, b-1, c-1, d-1]

sharks = []
sharks_pos = [[[-1, -1] for _ in range(N)] for __ in range(N)]

for y in range(N):
    for x in range(N):
        if start[y][x] > 0:
            sharks.append((y, x, start[y][x]-1, first[start[y][x]-1]-1))
            matrix[y][x] = [start[y][x]-1, k]
tc = 0
while tc <= 1000:
    if len(sharks) == 1:
        print(tc)
        break
    # for i in matrix:
    #     print(i)
    # print(len(sharks))

    for y, x, idx, dist in sharks:
        move_back = []
        chk = 0
        for i in range(4):
            if chk:
                break
            ny = y + dy[sharks_dir[idx][dist][i]]
            nx = x + dx[sharks_dir[idx][dist][i]]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[ny][nx][0] == -1:
                    if sharks_pos[ny][nx][0] != -1 and sharks_pos[ny][nx][0] < idx:
                        chk = 1
                        break
                    sharks_pos[ny][nx] = [idx, sharks_dir[idx][dist][i]]
                    break
                elif not move_back and matrix[ny][nx][0] == idx:
                    move_back = [ny, nx, idx, sharks_dir[idx][dist][i]]
        else:
            if move_back:
                sharks_pos[move_back[0]][move_back[1]] = [move_back[2], move_back[3]]
    tc += 1
    sharks = []
    for y in range(N):
        for x in range(N):
            if sharks_pos[y][x] != [-1, -1]:
                sharks.append((y, x, sharks_pos[y][x][0], sharks_pos[y][x][1]))
                matrix[y][x] = [sharks_pos[y][x][0], k]
                sharks_pos[y][x] = [-1, -1]
            elif matrix[y][x][1] > 0:
                matrix[y][x][1] -= 1
                if matrix[y][x][1] == 0:
                    matrix[y][x] = [-1, -1]
else:
    print(-1)