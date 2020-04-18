import sys
sys.stdin = open('인구 이동.txt')

from collections import deque

N, L, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

chk = 1
ans = 0
while chk:
    chk = 0
    visit = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visit[y][x]:
                q = deque()
                q.append((y, x))
                stack = [(y, x)]
                visit[y][x] = 1
                cnt = matrix[y][x]
                cnt2 = 1
                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx]:
                            if L <= abs(matrix[a][b]-matrix[ny][nx]) <= R:
                                q.append((ny, nx))
                                stack.append((ny, nx))
                                cnt += matrix[ny][nx]
                                cnt2 += 1
                                visit[ny][nx] = 1
                if cnt2 > 1:
                    chk = 1
                    for ny, nx in stack:
                        matrix[ny][nx] = cnt//cnt2
    if chk:
        ans += 1

print(ans)
