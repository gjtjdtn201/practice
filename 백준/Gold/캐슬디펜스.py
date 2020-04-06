import sys
sys.stdin = open('캐슬디펜스.txt', 'r')

from itertools import combinations
from collections import deque
from copy import deepcopy

def remain():
    for y in range(N):
        for x in range(M):
            if matrix2[y][x] == 1:
                q.append((y, x))

def fire():
    global cnt
    target = [(0, limit), (0, limit), (0, limit)]
    dist = [limit, limit, limit]
    while q:
        a, b = q.popleft()
        for i in range(3):
            z = abs(N-a) + abs(archer[i]-b)
            if dist[i] > z:
                dist[i] = z
                target[i] = (a, b)
            elif dist[i] == z and b < target[i][1]:
                target[i] = (a, b)

    for zz, (a, b) in enumerate(target):
        if matrix2[a][b] == 1:
            if dist[zz] <= D:
                matrix2[a][b] = 0
                cnt += 1

N, M, D = map(int, input().split())
matrix = deque(list(map(int, input().split())) for _ in range(N))
matrix.append([0]*M)
q = deque()
ans = 0
limit = N*M

for archer in combinations([i for i in range(M)], 3):
    matrix2 = deepcopy(matrix)
    cnt = 0
    while True:
        remain()
        if not q:
            break
        fire()
        matrix2.pop()
        matrix2.appendleft([0]*M)
    ans = max(ans, cnt)
print(ans)
