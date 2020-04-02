import sys
sys.stdin = open('보물섬.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline

def chk(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] == 'L':
            return True
    return False


R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

cnt = 0
q = deque()
for y in range(R):
    for x in range(C):
        if matrix[y][x] == 'L':
            if chk(y, x):
                q.append((y, x))
                visit = [[0] * C for __ in range(R)]
                visit[y][x] = 1
                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if 0 <= ny < R and 0 <= nx < C:
                            if matrix[ny][nx] == 'L' and not visit[ny][nx]:
                                q.append((ny, nx))
                                visit[ny][nx] = visit[a][b] + 1
                                cnt = max(cnt, visit[ny][nx])

print(cnt-1)