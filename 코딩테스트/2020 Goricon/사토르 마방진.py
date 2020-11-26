import sys
sys.stdin = open('사토르 마방진.txt')

import sys
input = sys.stdin.readline

N = int(input())

matrix = [list(input().rstrip()) for _ in range(N)]
def solution():
    for y in range(N):
        for x in range(y, N):
            if y == x:
                continue
            if matrix[y][x] != matrix[x][y]:
                return 'NO'
    return 'YES'
print(solution())