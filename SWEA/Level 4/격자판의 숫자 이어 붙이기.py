import sys
sys.stdin = open('격자판에 숫자 이어 붙이기.txt', 'r')

def ad(n, al, a, b):
    if n == 7:
        visit.add(al)
        return
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            ad(n+1, al+matrix[ny][nx], ny, nx)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for tc in range(1, int(input())+1):
    matrix = []
    for i in range(4):
        matrix.append(list(input().split()))
    visit = set()
    for y in range(4):
        for x in range(4):
            ad(1, matrix[y][x], y, x)
    print('#{} {}'.format(tc, len(visit)))