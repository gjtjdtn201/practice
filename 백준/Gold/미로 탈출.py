import sys
sys.stdin = open('미로 탈출.txt')

from collections import deque

def BFS():
    visit = [[[0, 0] for _ in range(M)] for __ in range(N)]
    q = deque()
    q.append((sty, stx, 1, 1))
    visit[sty][stx] = [1, 1]
    while q:
        a, b, c, d = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if (ny, nx) == (edy, edx):
                    print(d)
                    return
                if matrix[ny][nx] == 1 and c == 1 and not visit[ny][nx][1]:
                    q.append((ny, nx, 0, d+1))
                    visit[ny][nx][1] = 1
                elif matrix[ny][nx] == 0 and visit[ny][nx][c] == 0:
                    q.append((ny, nx, c, d+1))
                    visit[ny][nx][c] = 1
    print(-1)

N, M = map(int, input().split())

sty, stx = map(int, input().split())
edy, edx = map(int, input().split())
sty -= 1
stx -= 1
edy -= 1
edx -= 1
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

BFS()