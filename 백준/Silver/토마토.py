import sys
sys.stdin = open('토마토.txt', 'r')

from collections import deque

M, N = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

queue = deque()
cnt = 0
for i in matrix:
    if 0 in i:
        cnt += 1

dy = [1,-1,0,0]
dx = [0,0,1,-1]

# 모두 비어있을땐?
if cnt == 0:
    ans = 0
else:
    ans = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                queue.append((y,x))

    while queue:
        a, b = queue.popleft()
        for z in range(4):
            ny = a + dy[z]
            nx = b + dx[z]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 0:
                queue.append((ny, nx))
                matrix[ny][nx] = matrix[a][b] + 1

    for i in matrix:
        if 0 in i:
            ans = 0
            break
        if ans < max(i):
            ans = max(i)
    ans -= 1
print(ans)