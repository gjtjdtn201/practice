import sys
sys.stdin = open('벽돌 깨기.txt', 'r')

from copy import deepcopy
from collections import deque

def chk(matrix, n, cnt):
    global ans
    if cnt == 0:
        ans = 0
        return
    if n == N:
        cnt = 0
        for i in matrix:
            cnt += W - i.count(0)
        ans = min(cnt, ans)
        return
    for x in range(W):
        matrix2 = deepcopy(matrix)
        for y in range(H):
            if matrix[y][x] != 0:
                queue.append((y, x, matrix2[y][x]))
                matrix2[y][x] = 0
                boom(matrix2)
                cnt = fall(matrix2)
                chk(matrix2, n+1, cnt)
                break

def boom(c_matrix):
    while queue:
        a, b, pos = queue.popleft()
        for j in range(pos):
            for i in range(4):
                ny = a + dy[i] * j
                nx = b + dx[i] * j
                if 0 <= ny < H and 0 <= nx < W and c_matrix[ny][nx]:
                    if c_matrix[ny][nx] > 1:
                        queue.append((ny, nx, c_matrix[ny][nx]))
                    c_matrix[ny][nx] = 0

def fall(c_matrix):
    cnt = 0
    for x in range(W):
        stack = []
        for y in range(H):
            if c_matrix[y][x]:
                stack.append(c_matrix[y][x])
                cnt += 1
        idx = H - 1
        while stack:
            c_matrix[idx][x] = stack.pop()
            idx -= 1
        while idx >= 0:
            c_matrix[idx][x] = 0
            idx -= 1
    return cnt

for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    matrix = []
    for i in range(H):
        matrix.append(list(map(int, input().split())))
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    ans = 987654321
    chk2 = 0
    queue = deque()
    chk(matrix, 0, ans)
    print('#{} {}'.format(tc, ans))