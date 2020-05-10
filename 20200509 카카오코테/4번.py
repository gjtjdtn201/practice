from collections import deque

def solution(board):
    N = len(board)
    q = deque()
    q.append((0,0,2,-500))
    visit = [[-1]*N for _ in range(N)]
    visit[0][0] = -500
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    while q:
        a, b, c, d = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                price = 600 if c != i&1 else 100
                if visit[ny][nx] == -1:
                    q.append((ny, nx, i&1, d + price))
                    visit[ny][nx] = d + price
                elif visit[ny][nx] >= d + price:
                    q.append((ny, nx, i&1, d+price))
                    visit[ny][nx] = d + price
    return visit[N-1][N-1]

a = [[0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 0]]
print(solution(a))