import sys
sys.stdin = open('파이프 옮기기1.txt', 'r')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[[0]*3 for _ in range(N)] for __ in range(N)]
visit[0][1][0] = 1
for x in range(2, N):
    if matrix[0][x] == 0:
        visit[0][x][0] = visit[0][x-1][0]
for y in range(1, N):
    for x in range(2, N):
        if matrix[y][x]+matrix[y][x-1]+matrix[y-1][x] == 0:
            visit[y][x][2] = visit[y-1][x-1][0] + visit[y-1][x-1][1] + visit[y-1][x-1][2]
        if matrix[y][x] == 0:
            visit[y][x][0] = visit[y][x-1][0] + visit[y][x-1][2]
            visit[y][x][1] = visit[y-1][x][1] + visit[y-1][x][2]

print(sum(visit[N-1][N-1]))