import sys
sys.stdin = open('미로의 거리.txt', 'r')

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input())))

    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                sty, stx = y, x
                break

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    queue = deque()
    queue.append((sty,stx))
    visit = [[0 for _ in range(N)] for __ in range(N)]
    visit[sty][stx] = 1
    ans = 0
    while queue:
        a, b = queue.popleft()
        if matrix[a][b] == 3:
            ans = visit[a][b] - 2
            break
        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]
            if 0 <= y < N and 0 <= x < N and matrix[y][x] != 1 and visit[y][x] == 0:
                queue.append((y,x))
                visit[y][x] = visit[a][b] + 1

    print('#{} {}'.format(test_case, ans))