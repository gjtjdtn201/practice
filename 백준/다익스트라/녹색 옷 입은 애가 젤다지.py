import sys
sys.stdin = open('녹색 옷 입은 애가 젤다지.txt')

import sys
input = sys.stdin.readline
import heapq

def DSR(tc):
    q = []
    heapq.heappush(q, (matrix[0][0], 0, 0))
    visit[0][0] = 0
    while q:
        c, a, b = heapq.heappop(q)
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                tmp = c + matrix[ny][nx]
                if tmp < visit[ny][nx]:
                    heapq.heappush(q, (tmp, ny, nx))
                    visit[ny][nx] = tmp
                if (ny, nx) == (N - 1, N - 1):
                    print('Problem {}: {}'.format(tc, visit[ny][nx]))
                    return

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [[float('inf')]*N for _ in range(N)]
    DSR(tc)