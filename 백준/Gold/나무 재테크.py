import sys
sys.stdin = open('나무 재테크.txt', 'r')

from collections import deque

N, M, K = map(int, input().split())
A = [[5]*N for _ in range(N)]
A2 = [list(map(int, input().split())) for _ in range(N)]
q, qtmp, q2 = deque(), deque(), deque()
for __ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    q.append((x, y, z))

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

while K:
    K -= 1
    # 봄
    while q:
        a, b, c = q.popleft()
        if A[a][b] == 0:
            q2.append((a, b, c))
        else:
            A[a][b] -= c
            if A[a][b] < 0:
                A[a][b] += c
                q2.append((a, b, c))
            else:
                qtmp.append((a, b, c+1))
    # 여름
    while q2:
        a, b, c = q2.popleft()
        A[a][b] += c//2
    # 가을
    while qtmp:
        a, b, c = qtmp.popleft()
        if c%5 == 0:
            for i in range(8):
                ny = a + dy[i]
                nx = b + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    q.appendleft((ny, nx, 1))
        q.append((a, b, c))
    # 겨울
    for y in range(N):
        for x in range(N):
            A[y][x] += A2[y][x]
print(len(q))