import sys
sys.stdin = open('치킨 배달.txt')

from itertools import combinations

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for y in range(N):
    for x in range(N):
        if matrix[y][x] == 1:
            house.append((y, x))
        elif matrix[y][x] == 2:
            chicken.append((y, x))

ans = 987654321
for i in combinations(chicken, M):
    c_ans = 0
    for hy, hx in house:
        cnt = N*N+1
        for j in i:
            chk = abs(j[0]-hy)+abs(j[1]-hx)
            cnt = min(cnt, chk)
        c_ans += cnt
        if c_ans > ans:
            break
    ans = min(ans, c_ans)
print(ans)