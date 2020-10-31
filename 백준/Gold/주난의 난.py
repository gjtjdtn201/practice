import sys
sys.stdin = open('주난의 난.txt')

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    q, qtmp = deque(), deque()
    q.append((sty, stx))
    visit = [[0]*M for _ in range(N)]
    visit[sty][stx] = 1
    cnt = 0
    while True:
        cnt += 1
        while q:
            a, b = q.popleft()
            for i in range(4):
                ny = a + dy[i]
                nx = b + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
                    if matrix[ny][nx] == 2:
                        print(cnt)
                        return
                    elif matrix[ny][nx] == 1:
                        qtmp.append((ny, nx))
                        visit[ny][nx] = 1
                        matrix[ny][nx] = 0
                    else:
                        q.append((ny, nx))
                        visit[ny][nx] = 1
        q = qtmp
        qtmp = deque()

N, M = map(int, input().split())

sty, stx, edy, edx = map(int, input().split())
sty -= 1
stx -= 1
edy -= 1
edx -= 1

matrix = [list(input().rstrip()) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == '0':
            matrix[y][x] = 0
        elif matrix[y][x] == '1':
            matrix[y][x] = 1
        elif matrix[y][x] == '#':
            matrix[y][x] = 2
        else:
            matrix[y][x] = 0

if (sty, stx) == (edy, edx):
    print(0)
else:
    solution()

