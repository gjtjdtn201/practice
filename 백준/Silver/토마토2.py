import sys
sys.stdin = open('토마토2.txt', 'r')

from collections import deque

M, N, H = map(int, input().split())

matrix = []
cnt = 0
for __ in range(H):
    for _ in range(N):
        a = list(map(int, input().split()))
        matrix.append(a)

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

ans = -1

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if matrix[y+N*z][x] == 1:
                queue.append((y, x, z))
while queue:
    a, b, c = queue.popleft()
    for i in range(6):
        ny = a + dy[i]
        nx = b + dx[i]
        nz = c + dz[i]
        if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H and matrix[ny+N*nz][nx] == 0:
            queue.append((ny, nx, nz))
            matrix[ny+N*nz][nx] = matrix[a+N*c][b] + 1

for i in matrix:
    if 0 in i:
        ans = -1
        break
    elif ans < max(i)-1:
        ans = max(i)-1
print(ans)