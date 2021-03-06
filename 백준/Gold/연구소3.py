import sys
sys.stdin = open('연구소2.txt')

from collections import deque
from itertools import combinations

def BFS():
    global ans
    cnt = chk = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx]:
                if matrix[ny][nx] != 1:
                    q.append((ny, nx))
                    visit[ny][nx] = visit[a][b] + 1
                    if matrix[ny][nx] == 0:
                        chk += 1
                        cnt = max(visit[ny][nx], cnt)
    if chk == blank:
        ans = min(ans, cnt)

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

virus = []
blank = 0
for y in range(N):
    for x in range(N):
        if matrix[y][x] == 2:
            virus.append((y, x))
        elif matrix[y][x] == 0:
            blank += 1
ans = 987654321

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in combinations(range(len(virus)), M):
    q = deque()
    visit = [[0] * N for _ in range(N)]
    for j in i:
        q.append(virus[j])
        visit[virus[j][0]][virus[j][1]] = 1
    BFS()
if ans == 0:
    ans = 1
print(-1 if ans == 987654321 else ans-1)