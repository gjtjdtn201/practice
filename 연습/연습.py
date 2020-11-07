import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS():
    q = deque()
    q.append((sty - 1, stx - 1))
    visit[sty-1][stx-1] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and 0 <= ny+A < N and 0 <= nx+b < M and visit[ny][nx] == 0:
                if matrix[ny][nx] == 0 and visit[ny][nx] == 0:
                    if (ny, nx) == (edy-1, edx-1):
                        return visit[a][b]
                    q.append((ny, nx))
                    visit[ny][nx] = visit[a][b] + 1
    return -1

N, M, A, B, K = map(int,input().split())

matrix = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]

for i in range(K):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

sty, stx = map(int, input().split())
edy, edx = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

print(BFS())

for i in visit:
    print(i)
print()
for i in matrix:
    print(i)