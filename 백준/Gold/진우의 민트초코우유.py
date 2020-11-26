import sys
sys.stdin = open('진우의 민트초코우유.txt')

def DFS(a, b, c, d):
    global ans
    if a == 0 and c != 0:
        ans = max(ans, c-1)
        return
    for i in range(num):
        if cost[a][i] == 0 or i in d:
            continue
        if cost[a][i] <= b:
            d.append(i)
            DFS(i, b-cost[a][i]+H, c+1, d)
            d.pop()

N, M, H = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(N)]

home, milk, ans = [], [], 0

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 1:
            home.append([y, x])
        elif matrix[y][x] == 2:
            milk.append([y, x])
home.extend(milk)
num = len(home)
cost = [[0]*(num) for _ in range(num)]

for y in range(num):
    for x in range(num):
        if y == x:
            continue
        cost[y][x] = abs(home[y][0]-home[x][0]) + abs(home[y][1]-home[x][1])
        cost[x][y] = abs(home[y][0]-home[x][0]) + abs(home[y][1]-home[x][1])

# 위치, 체력, 카운트, 방문
DFS(0, M, 0, [])
print(ans)