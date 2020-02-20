import sys
sys.stdin = open('로봇 청소기.txt', 'r')

N, M = map(int, input().split())

r, c, d = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

stack = [(r, c)]
visit = set()
while stack:
    a, b = stack.pop()
    visit.add((a, b))
    for i in range(4):
        d -= 1
        if d < 0:
            d = 3
        ny = a + dy[d]
        nx = b + dx[d]
        if matrix[ny][nx] == 0 and (ny, nx) not in visit:
            stack.append((ny, nx))
            break
    else:
        p = d
        d += 2
        if d > 3:
            d -= 4
        ny = a + dy[d]
        nx = b + dx[d]
        if matrix[ny][nx] == 0:
            stack.append((ny, nx))
            d = p
        else:
            break
print(len(visit))