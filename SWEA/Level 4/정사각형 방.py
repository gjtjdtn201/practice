import sys
sys.stdin = open('정사각형 방.txt', 'r')

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ans = 0
    res = N**2
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if (N**2 - matrix[y][x]) < ans:
                continue
            if not visit[y][x]:
                stack = [(y, x)]
                cnt = chk = 0
                while stack:
                    a, b = stack.pop()
                    visit[a][b] = True
                    cnt += 1
                    for i in range(4):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == matrix[a][b] + 1:
                            stack.append((ny, nx))
                if ans < cnt:
                    ans = cnt
                    res = matrix[y][x]
                elif ans == cnt:
                    res = min(res, matrix[y][x])
    print('#{} {} {}'.format(test_case, res, ans))