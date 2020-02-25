import sys
sys.stdin = open('그림.txt', 'r')

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = cnt2 = ans = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1:
            matrix[y][x] = 0
            cnt += 1
            stack = [(y, x)]
            cnt2 = 0
            while stack:
                a, b = stack.pop()
                cnt2 += 1
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1:
                        stack.append((ny, nx))
                        matrix[ny][nx] = 0
            if cnt2 > ans:
                ans = cnt2
print(cnt)
print(ans)