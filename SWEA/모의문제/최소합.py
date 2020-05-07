import sys
sys.stdin = open('최소합.txt', 'r')

from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [[-1]*N for _ in range(N)]
    dy = [1, 0]
    dx = [0, 1]
    ans = 987654321
    q = deque()
    q.append((0, 0))
    visit[0][0] = matrix[0][0]
    while q:
        a, b = q.popleft()
        for i in range(2):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) == (N-1, N-1):
                    ans = min(ans, visit[a][b]+matrix[N-1][N-1])
                if visit[ny][nx] == -1 or visit[ny][nx] > visit[a][b] + matrix[ny][nx]:
                    q.append((ny, nx))
                    visit[ny][nx] = visit[a][b] + matrix[ny][nx]
    print('#{} {}'.format(tc, ans))