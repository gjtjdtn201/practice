import sys
sys.stdin = open('다리 만들기.txt')

from _collections import deque

def BFS(qtmp):
    chk = 1
    ans = 987654321
    q = deque()
    while chk:
        while qtmp:
            a, b, c = qtmp.popleft()
            matrix[a][b] = c
            for i in range(4):
                ny = a + dy[i]
                nx = b + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    # 자신이 아닌 새땅을 만나면 값 출력
                    if matrix[ny][nx] != 0 and matrix[ny][nx] != c:
                        chk = 0
                        ans = min(ans, visit[ny][nx]+visit[a][b]-2)
                    # 바다면 한칸씩 늘리기
                    if matrix[ny][nx] == 0 and visit[ny][nx] == 0:
                        q.append((ny, nx, c))
                        visit[ny][nx] = visit[a][b] + 1
        if not chk:
            print(ans)
            return
        qtmp = q
        q = deque()
N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

cnt = 1
qtmp = deque()
# 섬 숫자 라벨링 하기
for y in range(N):
    for x in range(N):
        if matrix[y][x] == 1:
            cnt += 1
            q = deque()
            q.append((y, x))
            visit[y][x] = 1
            matrix[y][x] = cnt
            while q:
                a, b = q.popleft()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        if matrix[ny][nx] == 1 and visit[ny][nx] == 0:
                            q.append((ny, nx))
                            visit[ny][nx] = 1
                            matrix[ny][nx] = cnt
                        # 바다면 tmp에 값을 넣기
                        elif matrix[ny][nx] == 0 and visit[ny][nx] == 0:
                            qtmp.append((ny, nx, cnt))
                            visit[ny][nx] = 2
BFS(qtmp)