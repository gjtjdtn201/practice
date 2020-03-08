import sys
sys.stdin = open('아기상어.txt', 'r')

from collections import deque

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
food = {}
for y in range(N):
    for x in range(N):
        if matrix[y][x] != 0:
            if matrix[y][x] not in food:
                food[matrix[y][x]] = (y, x)
            else:
                food[matrix[y][x]] += (y, x)
q = deque()
sty, stx = food[9]
matrix[sty][stx] = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
dis = []
size = cnt = 2
ans = 0
try:
    one = list(food[1])
    for i in range(0, len(one),2):
        dis.append((one[i], one[i+1]))
except KeyError:
    pass
while dis:
    chk = 0
    q.append((sty, stx))
    visit = [[0] * N for __ in range(N)]
    visit[sty][stx] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx]:
                if matrix[ny][nx] <= size:
                    visit[ny][nx] = visit[a][b] + 1
                    q.append((ny, nx))
                    chk = 1
    if chk == 0:
        break
    z = 99999
    dis.sort()
    for y, x in dis:
        if 0 < visit[y][x] < z:
            z = visit[y][x]
            sty, stx = y, x
    if z == 99999:
        break
    cnt -= 1
    if cnt == 0:
        size += 1
        cnt = size
        try:
            one = list(food[size-1])
            for i in range(0, len(one), 2):
                dis.append((one[i], one[i + 1]))
        except KeyError:
            pass
    matrix[sty][stx] = 0
    dis.remove((sty, stx))
    ans += (z-1)
    print(ans)
print(ans)
