import sys
sys.stdin = open('마인크래프트.txt', 'r')

N, M, B = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(N)]
ans = 999999999999

for i in range(256, -1, -1):
    build = remove = 0
    for y in range(N):
        for x in range(M):
            height = matrix[y][x] - i
            if height > 0:
                remove += height
            elif height < 0:
                build -= height
    if remove + B >= build:
        time = remove * 2 + build
        if ans > time:
            ans = time
            level = i

print(ans, level)
