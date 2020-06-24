import sys
sys.stdin = open('스타트 택시.txt')

from heapq import heappop, heappush
from collections import deque

N, M, fuel = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

q = []
sty, stx = map(int, input().split())
heappush(q, (0, sty-1, stx-1))
cos = [0]
for i in range(1, M+1):
    a, b, c, d = map(int, input().split())
    matrix[a-1][b-1] = -i
    cos.append((a-1, b-1, c-1, d-1))
chk, chk2 = 0, 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

visit = [[0]*N for _ in range(N)]

while q:
    if M == 0:
        break
    dist, sy, sx = heappop(q)
    if matrix[sy][sx] < 0:
        fuel -= dist
        if fuel < 0:
            break
        dq = deque()
        dq.append((sy, sx, 0))
        visit2 = [[0]*N for _ in range(N)]
        chk, chk2 = 0, 0
        while dq:
            if chk or chk2:
                break
            y, x, cnt = dq.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] < 1 and not visit2[ny][nx]:
                    if (ny, nx) == (cos[-matrix[sy][sx]][2], cos[-matrix[sy][sx]][3]):
                        fuel -= (cnt+1)
                        if fuel < 0:
                            chk = 1
                            break
                        M -= 1
                        fuel += (cnt+1)*2
                        q.clear()
                        matrix[sy][sx] = 0
                        heappush(q, (0, ny, nx))
                        chk2 = 1
                        visit = [[0] * N for _ in range(N)]
                        break
                    dq.append((ny, nx, cnt+1))
                    visit2[ny][nx] = 1
    if chk:
        break
    if chk2:
        chk2 = 0
        continue
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] < 1 and not visit[ny][nx]:
            visit[ny][nx] = 1
            heappush(q, (dist+1, ny, nx))
print(fuel) if M == 0 else print(-1)