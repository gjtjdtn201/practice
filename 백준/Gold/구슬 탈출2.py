import sys
sys.stdin = open('구슬 탈출2.txt')

import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 'O':
            hole = [y, x]
        elif matrix[y][x] == 'R':
            red = [y, x]
            matrix[y][x] = '.'
        elif matrix[y][x] == 'B':
            blue = [y, x]
            matrix[y][x] == '.'
