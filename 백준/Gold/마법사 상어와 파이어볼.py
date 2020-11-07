import sys
sys.stdin = open('마법사 상어와 파이어볼.txt')

N, M, K = map(int, input().split())

balls = []

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

# r 가로, c 세로, m 질량, d 방향, s 속력
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    balls.append([r-1, c-1, m, s, d])

for round in range(K):
    if not balls:
        break
    matrix = [[[] for _ in range(N)] for __ in range(N)]
    for r, c, m, s, d in balls:
        ny = (r + dy[d]*s + N) % N
        nx = (c + dx[d]*s + N) % N
        matrix[ny][nx].append([m, s, d])
    balls = []
    for y in range(N):
        for x in range(N):
            if len(matrix[y][x]) >= 2:
                m, s, chk1, chk2 = 0, 0, 0, 0
                for nm, ns, nd in matrix[y][x]:
                    m += nm
                    s += ns
                    if nd % 2:
                        chk1 = 1
                    else:
                        chk2 = 1
                if m < 5:
                    continue
                else:
                    m = m // 5
                    s = s // len(matrix[y][x])
                    chk3 = [0, 2, 4, 6]
                    if (chk1, chk2) == (1, 1):
                        chk3 = [1, 3, 5, 7]
                    for i in chk3:
                        balls.append([y, x, m, s, i])
            elif not matrix[y][x] == []:
                balls.append([y, x, matrix[y][x][0][0], matrix[y][x][0][1], matrix[y][x][0][2]])
ans = 0
for i in balls:
    ans += i[2]
print(ans)