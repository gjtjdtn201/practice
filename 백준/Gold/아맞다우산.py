import sys
sys.stdin = open('아맞다우산.txt')

from collections import deque

def permutation(n):
    global ans
    if n == K:
        perm = a[:]
        ans = min(ans, solution(perm))
    for i in range(K):
        if i_visit[i]:
            continue
        a[n] = i
        i_visit[i] = 1
        permutation(n + 1)
        i_visit[i] = 0

def solution(perm):
    global ans
    perm.append(K)
    cnt = 0
    sy, sx = sty, stx
    for i in perm:
        if cnt >= ans:
            return cnt
        chk = 0
        py, px = items[i]
        visit = [[0]*N for _ in range(M)]
        q = deque()
        q.append((sy, sx))
        visit[sy][sx] = 1
        while q:
            if chk:
                break
            a, b = q.popleft()
            for j in range(4):
                ny = a + dy[j]
                nx = b + dx[j]
                if 0 <= ny < M and 0 <= nx < N and matrix[ny][nx] == '.' and not visit[ny][nx]:
                    if (ny, nx) == (py, px):
                        cnt += visit[a][b]
                        chk = 1
                        break
                    q.append((ny, nx))
                    visit[ny][nx] = visit[a][b] + 1
        sy, sx = py, px
    return cnt


N, M = map(int, input().split())

matrix = [list(input()) for _ in range(M)]

items = []
for y in range(M):
    for x in range(N):
        if matrix[y][x] == 'X':
            items.append((y, x))
            matrix[y][x] = '.'
        elif matrix[y][x] == 'E':
            edy, edx = y, x
            matrix[y][x] = '.'
        elif matrix[y][x] == 'S':
            sty, stx = y, x
            matrix[y][x] = '.'
K = len(items)
items.append((edy, edx))
a = [0]*K
i_visit = [0]*K
ans = float('inf')

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

permutation(0)
print(ans)