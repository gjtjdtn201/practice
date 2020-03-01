import sys
sys.stdin = open('적록색약.txt', 'r')

import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(input()))
matrix2 = deepcopy(matrix)
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = cnt2 = 0
for y in range(N):
    for x in range(N):
        if matrix[y][x] != 0:
            word = matrix[y][x]
            stack = [(y, x)]
            matrix[y][x] = 0
            cnt += 1
            while stack:
                a, b = stack.pop()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == word:
                        stack.append((ny, nx))
                        matrix[ny][nx] = 0
for y in range(N):
    for x in range(N):
        if matrix2[y][x] != 0:
            word = matrix2[y][x]
            if word in ['R', 'G']:
                word = ['R', 'G']
            else:
                word = list(word)
            stack = [(y, x)]
            matrix2[y][x] = 0
            cnt2 += 1
            while stack:
                a, b = stack.pop()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and matrix2[ny][nx] in word:
                        stack.append((ny, nx))
                        matrix2[ny][nx] = 0
print(cnt, cnt2)