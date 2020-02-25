import sys
sys.stdin = open('유기농 배추.txt', 'r')

T = int(input())

for test_case in range(T):
    M, N, K = map(int, input().split())

    matrix = [[0] * M for _ in range(N)]

    for i in range(K):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    cnt = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                cnt += 1
                stack = [(y, x)]
                while stack:
                    a, b = stack.pop()
                    for i in range(4):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 1:
                            stack.append((ny, nx))
                            matrix[ny][nx] = 0
    print(cnt)