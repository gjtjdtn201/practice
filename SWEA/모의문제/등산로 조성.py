import sys
sys.stdin = open('등산로 조성.txt', 'r')

def DFS(y, x, cnt, K):
    global ans
    if ans < cnt:
        ans = cnt
    visit[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
            if matrix[ny][nx] < matrix[y][x]:
                DFS(ny, nx, cnt+1, K)
            elif matrix[ny][nx] - K < matrix[y][x]:
                dig = matrix[ny][nx]
                matrix[ny][nx] = matrix[y][x] - 1
                DFS(ny, nx, cnt+1, 0)
                matrix[ny][nx] = dig
    visit[y][x] = 0

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    matrix = []
    cnt = 0
    for i in range(N):
        a = list(map(int, input().split()))
        matrix.append(a)
        if max(a) > cnt:
            cnt = max(a)

    visit = [[0]*N for _ in range(N)]
    high = []
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == cnt:
                high.append((y, x))

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    ans = 0
    while high:
        a, b = high.pop()
        DFS(a, b, 0, K)

    print('#{} {}'.format(test_case, ans+1))
