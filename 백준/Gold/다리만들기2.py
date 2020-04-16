import sys
sys.stdin = open('다리만들기2.txt')

from collections import deque

def bridge():
    for y in range(N):
        for x in range(M-3):
            if matrix[y][x] != 0 and matrix[y][x+1] == 0:
                nx = x+1
                # cnt2 = 다리의 갯수
                cnt2 = 0
                while nx < M:
                    if matrix[y][nx] == 0:
                        nx += 1
                        cnt2 += 1
                    else:
                        if cnt2 > 1:
                            a = matrix[y][x]-2
                            b = matrix[y][nx]-2
                            if island[a][b] == 0:
                                island[a][b] = cnt2
                                island[b][a] = cnt2
                            elif island[a][b] > cnt2:
                                island[a][b] = cnt2
                                island[b][a] = cnt2
                        break
    for x in range(M):
        for y in range(N-3):
            if matrix[y][x] != 0 and matrix[y+1][x] == 0:
                ny = y+1
                cnt2 = 0
                while ny < N:
                    if matrix[ny][x] == 0:
                        ny += 1
                        cnt2 += 1
                    else:
                        if cnt2 > 1:
                            a = matrix[y][x]-2
                            b = matrix[ny][x]-2
                            if island[a][b] == 0:
                                island[a][b] = cnt2
                                island[b][a] = cnt2
                            elif island[a][b] > cnt2:
                                island[a][b] = cnt2
                                island[b][a] = cnt2
                        break

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = 1
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            cnt += 1
            q = deque()
            q.append((y, x))
            matrix[y][x] = cnt
            while q:
                a, b = q.popleft()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 1:
                        q.append((ny, nx))
                        matrix[ny][nx] = cnt

K = cnt-1
island = [[0]*K for _ in range(K)]

bridge()

for i in island:
    print(i)

ans = -1
chk = [0]*K
for i in range(K):
    for j in range(i+1, K):
        if island[i][j] == 0:
            continue
        if chk[j] == 0 or chk[i] == 0:
            chk[i] = island[i][j]
            chk[j] = island[i][j]
        elif chk[j] > island[i][j] or chk[i] > island[i][j]:
            chk[i] = island[i][j]
            chk[j] = island[i][j]

print(chk)

if chk.count(0) == 0:
    ans = sum(chk)

print(ans)


