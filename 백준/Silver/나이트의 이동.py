import sys
sys.stdin = open('나이트의 이동.txt', 'r')

import sys
input = sys.stdin.readline
from collections import deque

dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [2, 1, -1, -2, -2, -1, 1, 2]

for test_case in range(int(input())):
    L = int(input())
    matrix = [[0] * L for _ in range(L)]
    sty, stx = map(int, input().split())
    edy, edx = map(int, input().split())
    queue = deque()
    queue.append((sty, stx))
    matrix[sty][stx] = 1
    ans = 0
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < L and 0 <= nx < L and matrix[ny][nx] == 0:
                queue.append((ny, nx))
                matrix[ny][nx] = matrix[a][b] + 1
                if (ny, nx) == (edy, edx):
                    ans = matrix[ny][nx] - 1
                    break
    print(ans)