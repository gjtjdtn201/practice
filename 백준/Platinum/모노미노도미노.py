import sys
sys.stdin = open('모노미노도미노.txt')

import sys
input = sys.stdin.readline

N = int(input())
matrix = [[0]*10 for _ in range(10)]
ans = 0
for _ in range(1, N+1):
    t, y, x = map(int, input().split())
    if t == 1:
        # 파란색이동
        bx, by = x, y
        while bx < 9:
            bx += 1
            if matrix[by][bx] > 0:
                matrix[by][bx-1] = _
                break
        else:
            matrix[by][9] = _
        # 초록색 이동
        gx, gy = x, y
        while gy < 9:
            gy += 1
            if matrix[gy][gx] > 0:
                matrix[gy-1][gx] = _
                break
        else:
            matrix[9][gx] = _
    elif t == 3:
        # 파란색이동
        bx, by = x, y
        while bx < 9:
            bx += 1
            if matrix[by][bx] > 0 or matrix[by+1][bx] > 0:
                matrix[by][bx - 1] = _
                matrix[by+1][bx - 1] = _
                break
        else:
            matrix[by][9] = _
            matrix[by+1][9] = _
        # 초록색 이동
        gx, gy = x, y
        gy += 1
        while gy < 9:
            gy += 1
            if matrix[gy][gx] > 0:
                matrix[gy - 1][gx] = _
                matrix[gy - 2][gx] = _
                break
        else:
            matrix[9][gx] = _
            matrix[8][gx] = _
    else:
        # 파란색이동
        bx, by = x, y
        bx += 1
        while bx < 9:
            bx += 1
            if matrix[by][bx] > 0:
                matrix[by][bx - 1] = _
                matrix[by][bx - 2] = _
                break
        else:
            matrix[by][9] = _
            matrix[by][8] = _
        # 초록색 이동
        gx, gy = x, y
        while gy < 9:
            gy += 1
            if matrix[gy][gx] > 0 or matrix[gy][gx + 1] > 0:
                matrix[gy - 1][gx] = _
                matrix[gy - 1][gx + 1] = _
                break
        else:
            matrix[9][gx] = _
            matrix[9][gx+1] = _

    # 초록색
    chk = 1
    while chk:
        chk = 0
        for y in range(6, 10):
            x = 0
            if matrix[y][x] > 0:
                for x in range(1, 4):
                    if matrix[y][x] == 0:
                        break
                else:
                    ans += 1
                    chk = 1
                    for x in range(4):
                        matrix[y][x] = 0
        if chk:
            for y in range(8, 3, -1):
                for x in range(4):
                    if matrix[y][x] > 0:
                        if matrix[y][x] == matrix[y][x+1]:
                            ny = y + 1
                            while ny < 10:
                                if matrix[ny][x] > 0 or matrix[ny][x+1] > 0:
                                    if ny - 1 != y:
                                        matrix[ny - 1][x] = matrix[y][x]
                                        matrix[ny - 1][x + 1] = matrix[y][x + 1]
                                        matrix[y][x], matrix[y][x+1] = 0, 0
                                    break
                                ny += 1
                            else:
                                matrix[9][x] = matrix[y][x]
                                matrix[9][x+1] = matrix[y][x+1]
                                matrix[y][x], matrix[y][x+1] = 0, 0
                        else:
                            ny = y + 1
                            while ny < 10:
                                if matrix[ny][x] > 0:
                                    if ny-1 != y:
                                        matrix[ny-1][x] = matrix[y][x]
                                        matrix[y][x] = 0
                                    break
                                ny += 1
                            else:
                                matrix[9][x] = matrix[y][x]
                                matrix[y][x] = 0
    gcnt = 0
    for y in range(4, 6):
        for x in range(4):
            if matrix[y][x] > 0:
                gcnt += 1
                break
    if gcnt > 0:
        for y in range(10-gcnt, 10):
            for x in range(4):
                matrix[y][x] = 0
        for y in range(9-gcnt, 3, -1):
            for x in range(4):
                if matrix[y][x] > 0:
                    matrix[y+gcnt][x], matrix[y][x] = matrix[y][x], matrix[y+gcnt][x]

    # 파란색
    chk = 1
    while chk:
        chk = 0
        for x in range(6, 10):
            y = 0
            if matrix[y][x] > 0:
                for y in range(1, 4):
                    if matrix[y][x] == 0:
                        break
                else:
                    ans += 1
                    chk = 1
                    for y in range(4):
                        matrix[y][x] = 0
        if chk:
            for x in range(8, 3, -1):
                for y in range(4):
                    if matrix[y][x] > 0:
                        if matrix[y][x] == matrix[y+1][x]:
                            nx = x + 1
                            while nx < 10:
                                if matrix[y][nx] > 0 or matrix[y+1][nx] > 0:
                                    if nx - 1 != x:
                                        matrix[y][nx - 1] = matrix[y][x]
                                        matrix[y + 1][nx - 1] = matrix[y+1][x]
                                        matrix[y][x], matrix[y+1][x] = 0, 0
                                    break
                                nx += 1
                            else:
                                matrix[y][9] = matrix[y][x]
                                matrix[y+1][9] = matrix[y+1][x]
                                matrix[y][x], matrix[y+1][x] = 0, 0
                        else:
                            nx = x + 1
                            while nx < 10:
                                if matrix[y][nx] > 0:
                                    if nx - 1 != x:
                                        matrix[y][nx-1] = matrix[y][x]
                                        matrix[y][x] = 0
                                    break
                                nx += 1
                            else:
                                matrix[y][9] = matrix[y][x]
                                matrix[y][x] = 0
    bcnt = 0
    for x in range(4, 6):
        for y in range(4):
            if matrix[y][x] > 0:
                bcnt += 1
                break
    if bcnt > 0:
        for x in range(10 - bcnt, 10):
            for y in range(4):
                matrix[y][x] = 0
        for x in range(9 - bcnt, 3, -1):
            for y in range(4):
                if matrix[y][x] > 0:
                    matrix[y][x+bcnt], matrix[y][x] = matrix[y][x], matrix[y][x+bcnt]

    # for i in matrix :
    #     print(i)
    # print(ans)

cnt = 0
for y in range(6, 10):
    for x in range(4):
        if matrix[y][x] > 0:
            cnt += 1
        if matrix[x][y] > 0:
            cnt += 1
print(ans)
print(cnt)