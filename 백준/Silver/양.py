import sys
sys.stdin = open('양.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(R)]
visit = [[0]*C for __ in range(R)]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans1 = ans2 = 0
q = deque()
for y in range(R):
    for x in range(C):
        if matrix[y][x] != '#' and not visit[y][x]:
            wolf = sheep = 0
            q.append((y, x))
            visit[y][x] = 1
            if matrix[y][x] == 'v':
                wolf += 1
            elif matrix[y][x] == 'o':
                sheep += 1
            while q:
                a, b = q.popleft()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] != '#' and not visit[ny][nx]:
                        q.append((ny, nx))
                        visit[ny][nx] = 1
                        if matrix[ny][nx] == 'v':
                            wolf += 1
                        elif matrix[ny][nx] == 'o':
                            sheep += 1
            if wolf < sheep:
                ans1 += sheep
                wolf = 0
            ans2 += wolf
print(ans1, ans2)
