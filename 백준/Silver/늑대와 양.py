import sys
sys.stdin = open("늑대와 양.txt")

import sys
input = sys.stdin.readline

def solution():
    global chk
    for y in range(R):
        for x in range(C):
            if matrix[y][x] == '.':
                matrix[y][x] = 'D'
            elif matrix[y][x] == 'W':
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] == 'S':
                        chk = 0
                        return

R, C = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(R)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

chk = 1
solution()
print(chk)
if chk:
    for i in matrix:
        print(''.join(i))