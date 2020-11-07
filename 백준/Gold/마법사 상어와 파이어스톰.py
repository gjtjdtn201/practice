import sys
sys.stdin = open('마법사 상어와 파이어스톰.txt')

from collections import deque

N, Q = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(2**N)]

storm = list(map(int, input().split()))

dy = [0, 1, 0, -1, 0]
dx = [1, 0, -1, 0, 1]

def spin(y, x, level):
    if level < 0:
        return
    ny, nx = y, x+level
    for i in range(4):
        for j in range(level):
            y += dy[i]
            x += dx[i]
            ny += dy[i+1]
            nx += dx[i+1]
            n_matrix[ny][nx] = matrix[y][x]
    spin(y+1, x+1, level-2)

for i in range(Q):
    L = storm[i]
    if L > 0:
        n_matrix = [[0] * (2 ** N) for _ in range(2 ** N)]
        for y in range(0, 2**N, 2**L):
            for x in range(0, 2**N, 2**L):
                spin(y, x, 2**L-1)
        matrix = n_matrix
    # 얼음 녹이기
    ice_matrix = [[0]*(2**N) for _ in range(2**N)]
    ans = 0
    for y in range(2**N):
        for x in range(2**N):
            if matrix[y][x] == 0:
                continue
            cnt = 0
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < 2**N and 0 <= nx < 2**N and not matrix[ny][nx] == 0:
                    cnt += 1
            if cnt < 3:
                ice_matrix[y][x] = matrix[y][x] - 1
            else:
                ice_matrix[y][x] = matrix[y][x]
            ans += ice_matrix[y][x]
    # 매트릭스 바꾸기
    matrix = ice_matrix

visit = [[0]*(2**N) for _ in range(2**N)]
res = 0
for y in range(2**N):
    for x in range(2**N):
        if visit[y][x] == 0 and not matrix[y][x] == 0:
            cnt = 1
            q = deque()
            q.append((y, x))
            visit[y][x] = 1
            while q:
                a, b = q.pop()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N and not matrix[ny][nx] == 0:
                        if visit[ny][nx] == 0:
                            q.append((ny, nx))
                            visit[ny][nx] = 1
                            cnt += 1
            res = max(res, cnt)

print(ans)
print(res)