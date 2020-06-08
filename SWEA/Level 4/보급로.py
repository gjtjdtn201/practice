import sys
sys.stdin = open('보급로.txt')

from heapq import heappush, heappop

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def DSR():
    q = []
    heappush(q, (matrix[0][0], 0, 0))
    visit[0][0] = 0
    while q:
        c, a, b = heappop(q)
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                tmp = c + matrix[ny][nx]
                if tmp < visit[ny][nx]:
                    heappush(q, (tmp, ny, nx))
                    visit[ny][nx] = tmp
                if (ny, nx) == (N - 1, N - 1):
                    return visit[ny][nx]

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visit = [[float('inf')]*N for _ in range(N)]
    print('#{} {}'.format(tc, DSR()))