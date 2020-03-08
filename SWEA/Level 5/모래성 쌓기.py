import sys
sys.stdin = open('모래성 쌓기.txt', 'r')

from collections import deque

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    ans = -1
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    chk = 1
    q, qtmp = deque(), deque()
    for y in range(H):
        for x in range(W):
            if matrix[y][x] == '.':
                q.append((y, x))
            else:
                matrix[y][x] = int(matrix[y][x])
    if q:
        while chk:
            chk = 0
            while q:
                a, b = q.popleft()
                for i in range(8):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < H and 0 <= nx < W and matrix[ny][nx] != '.' and matrix[ny][nx] != 9:
                        matrix[ny][nx] -= 1
                        if matrix[ny][nx] == 0:
                            qtmp.append((ny, nx))
                            matrix[ny][nx] = '.'
                            chk = 1
            ans += 1
            q = deque(qtmp)
            qtmp = deque()
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))