import sys
sys.stdin = open('배열돌리기4.txt')

from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321
q = []
for i in range(K):
    q.append(tuple(map(int, input().split())))

for i in permutations(q):
    matrix2 = deepcopy(matrix)
    for j in i:
        # r세로, c가로위치, s회전횟수
        r, c, s = j
        for z in range(s, 0, -1):
            y1, x1, y2, x2 = r-z-1, c-z-1, r+z-1, c+z-1
            tmp = matrix2[y1][x1]
            ny = y1
            while ny<y2:
                matrix2[ny][x1] = matrix2[ny+1][x1]
                ny += 1
            nx = x1
            while nx<x2:
                matrix2[y2][nx] = matrix2[y2][nx+1]
                nx += 1
            ny = y2
            while ny>y1:
                matrix2[ny][x2] = matrix2[ny-1][x2]
                ny -= 1
            nx = x2
            while nx>x1+1:
                matrix2[y1][nx] = matrix2[y1][nx-1]
                nx -= 1
            matrix2[y1][nx] = tmp
    for k in matrix2:
        ans = min(ans,sum(k))
print(ans)