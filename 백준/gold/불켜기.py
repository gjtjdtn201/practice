import sys
sys.stdin = open('불켜기.txt', 'r')

from collections import deque

def lightchk(a, b):
    global cnt
    for j in light:
        if a == j[0] and b == j[1]:
            poss[j[2]][j[3]] = 1


N, M = map(int, input().split())

matrix = [[0] * N for _ in range(N)]
poss = [[0] * N for _ in range(N)]

light = []
for i in range(M):
    x, y, a, b = map(int, input().split())
    light.append((x-1, y-1, a-1, b-1))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
queue = deque()
queue.append((0, 0))
lightchk(0, 0)
poss[0][0] = 1
matrix[0][0] = 1
visit = set()
while queue:
    chk = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[ny][nx] == 0:
                    visit.add((ny, nx))
    zz = list(visit)
    for z in zz:
        if poss[z[0]][z[1]] == 1:
            matrix[z[0]][z[1]] = 1
            chk = 1
            lightchk(z[0], z[1])
            queue.append((z[0], z[1]))
            zz.remove(z)
    if chk == 0:
        break
    visit = set(zz)
cnt = 0
for i in poss:
    cnt += i.count(1)
print(cnt)