import sys
sys.stdin = open('숫자판 점프.txt')

def solution(a, b, num):
    if len(num) == 6:
        ans.add(num)
        return
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            solution(ny, nx, num + matrix[ny][nx])

matrix = [list(map(str, input().split())) for _ in range(5)]

ans = set()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for y in range(5):
    for x in range(5):
        solution(y, x, matrix[y][x])
print(len(ans))