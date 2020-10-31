from collections import deque

v = [[0,0,1],[2,2,1],[0,0,0]]
answer = [0, 0, 0]
visit = [[0] * len(v) for _ in range(len(v))]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N = len(v)
for y in range(N):
    for x in range(N):
        if visit[y][x] == 0:
            q = deque()
            color = v[y][x]
            visit[y][x] = 1
            q.append((y, x))
            while q:
                a, b = q.pop()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and v[ny][nx] == color and visit[ny][nx] == 0:
                        q.append((ny, nx))
                        visit[ny][nx] = 1
            answer[color] += 1
print(answer)