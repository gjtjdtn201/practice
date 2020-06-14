import sys
sys.stdin = open('벽 부수고 이동하기 4.txt')

from collections import deque
import sys
input = sys.stdin.readline

def BFS(sty, stx, color):
    q = deque()
    q.append((sty, stx))
    visit[sty][stx] = color
    cnt = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not matrix[ny][nx]:
                if visit[ny][nx] == -1:
                    q.append((ny, nx))
                    visit[ny][nx] = color
                    cnt += 1
    return cnt


N, M = map(int, input().split())

matrix = [list(map(int, input().rstrip())) for _ in range(N)]

visit = [[-1]*M for __ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

color = 0
wall = []
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 0 and visit[y][x] == -1:
            wall.append(BFS(y, x, color))
            color += 1

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            ans = 1
            s = set()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not matrix[ny][nx]:
                    s.add(visit[ny][nx])
            for j in s:
                ans += wall[j]
            print(ans%10, end='')
        else:
            print(0, end='')
    print()