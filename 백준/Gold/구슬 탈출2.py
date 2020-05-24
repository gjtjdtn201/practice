import sys
sys.stdin = open('구슬 탈출2.txt')

import sys
# input = sys.stdin.readline

def DFS(chk, cnt):
    # 통과 했다면? 리턴
    for i in range(4):
        DFS(i, cnt+ 1)

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]

# 위, 아래, 왼, 오른
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

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
DFS(0, 0)