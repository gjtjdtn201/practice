import sys
sys.stdin = open('영역 구하기.txt', 'r')

M, N, K = map(int, input().split())

matrix = [[0 for _ in range(N)] for __ in range(M)]

for i in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry):
        for x in range(lx, rx):
            matrix[y][x] = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans = []
cnt2 = 0
for y in range(M):
    for x in range(N):
        if matrix[y][x] == 0:
            matrix[y][x] = 1
            cnt2 += 1
            stack = [(y, x)]
            cnt = 0
            while stack:
                a, b = stack.pop()
                cnt += 1
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < M and 0 <= nx < N and matrix[ny][nx] == 0:
                        stack.append((ny, nx))
                        matrix[ny][nx] = 1
            ans.append(cnt)
print(cnt2)
ans.sort()
print(*ans)