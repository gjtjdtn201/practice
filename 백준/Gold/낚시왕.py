import sys
sys.stdin = open('낚시왕.txt', 'r')

from collections import deque

R, C, M = map(int, input().split())
if M == 0:
    cnt = 0
else:
    matrix = [[0]*C for _ in range(R)]

    q = deque()

    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        matrix[r-1][c-1] = [s, d, z]

    cnt = 0
    for i in range(C):
        for zz in matrix:
            print(zz)
        print()
        for w in range(R):
            if matrix[w][i] != 0:
                cnt += matrix[w][i][2]
                matrix[w][i] = 0
                break
        if i == C-1:
            break
        for y in range(R):
            for x in range(C):
                if matrix[y][x] != 0:
                    q.append((y, x, matrix[y][x][0], matrix[y][x][1], matrix[y][x][2]))
                    matrix[y][x] = 0
        while q:
            r, c, s, d, z = q.popleft()
            if d == 1 or d == 2:
                if d == 1:
                    r -= s
                elif d == 2:
                    r += s
                while (r < 0 or r >= R):
                    if r < 0:
                        r = abs(r)
                        d = 2
                    elif r >= R:
                        r = 2*(R-1)-r
                        d = 1
            elif d == 3 or d == 4:
                if d == 3:
                    c += s
                elif d == 4:
                    c -= s
                while (c < 0 or c >= C):
                    if c < 0:
                        c = abs(c)
                        d = 3
                    elif c >= C:
                        c = 2*(C-1)-c
                        d = 4
            if matrix[r][c] == 0:
                matrix[r][c] = [s, d, z]
            elif matrix[r][c][2] < z:
                matrix[r][c] = [s, d, z]

print(cnt)