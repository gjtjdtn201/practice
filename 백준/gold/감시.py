import sys
sys.stdin = open('감시.txt', 'r')

from copy import deepcopy

def checking(c_matrix, cctvs, idx):
    global ans
    if idx == len(cctvs):
        cnt = 0
        for i in c_matrix:
            cnt += i.count(0)
        ans = min(ans, cnt)
        return
    y, x, cctv = cctvs[idx]
    if cctv == 1:
        for i in [[0], [1], [2], [3]]:
            next = checkmap(c_matrix, i, y, x)
            checking(next, cctvs, idx+1)
    elif cctv == 2:
        for i in [(0, 2), (1, 3)]:
            next = checkmap(c_matrix, i, y, x)
            checking(next, cctvs, idx+1)
    elif cctv == 3:
        for i in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            next = checkmap(c_matrix, i, y, x)
            checking(next, cctvs, idx+1)
    elif cctv == 4:
        for i in [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]:
            next = checkmap(c_matrix, i, y, x)
            checking(next, cctvs, idx+1)
    elif cctv == 5:
        next = checkmap(c_matrix, (0, 1, 2, 3), y, x)
        checking(next, cctvs, idx+1)

def checkmap(maps, chk, y, x):
    maps = deepcopy(maps)
    for k in chk:
        if k == 0:
            for z in range(x, M):
                if maps[y][z] == 0:
                    maps[y][z] = -1
                elif maps[y][z] == 6:
                    break
        if k == 1:
            for z in range(y, N):
                if maps[z][x] == 0:
                    maps[z][x] = -1
                elif maps[z][x] == 6:
                    break
        if k == 2:
            for z in range(x, -1, -1):
                if maps[y][z] == 0:
                    maps[y][z] = -1
                elif maps[y][z] == 6:
                    break
        if k == 3:
            for z in range(y, -1, -1):
                if maps[z][x] == 0:
                    maps[z][x] = -1
                elif maps[z][x] == 6:
                    break
    return maps
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

cctvs = []

for y in range(N):
    for x in range(M):
        if 1 <= matrix[y][x] < 6:
            cctvs.append((y, x, matrix[y][x]))

matrix2 = deepcopy(matrix)
ans = N * M
checking(matrix2, cctvs, 0)
print(ans)