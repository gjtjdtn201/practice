import sys
sys.stdin = open('말이 되고픈 원숭이.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    while queue:
        a, b, jump = queue.popleft()
        if a == H-1 and b == W-1:
            print(visit[a][b][jump]-1)
            return
        if jump < K:
            monkey(a, b, jump)
            horse(a, b, jump)
        elif jump == K:
            monkey(a, b, jump)
    print(-1)

def monkey(a, b, jump):
    for i in range(8, 12):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < H and 0 <= nx < W and matrix[ny][nx] == 0 and visit[ny][nx][jump] == 0:
            queue.append((ny, nx, jump))
            visit[ny][nx][jump] = visit[a][b][jump] + 1

def horse(a, b, jump):
    for i in range(8):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < H and 0 <= nx < W and matrix[ny][nx] == 0 and visit[ny][nx][jump+1] == 0:
            queue.append((ny, nx, jump + 1))
            visit[ny][nx][jump + 1] = visit[a][b][jump] + 1

K = int(input())
W, H = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(H)]
visit = [[[0]*(K+1) for _ in range(W)] for __ in range(H)]
visit[0][0][0] = 1

dy = [-2, -1, 1, 2, 2, 1, -1, -2, 0, 0, 1, -1]
dx = [1, 2, 2, 1, -1, -2, -2, -1, 1, -1, 0, 0]

queue = deque()
queue.append((0, 0, 0))
BFS()