import sys
sys.stdin = open('치킨 배달.txt')

def find(n, k):
    global ans
    if n == M:
        ans = min(ans, dis())
        return
    for i in range(k, len(chicken)):
        choose.append(chicken[i])
        find(n+1, i+1)
        choose.pop()

def dis():
    global ans
    c_ans = 0
    for hy, hx in house:
        cnt = N*N+1
        for cy, cx in choose:
            chk = abs(hy-cy) + abs(hx-cx)
            cnt = min(cnt, chk)
        c_ans += cnt
        if c_ans > ans:
            return ans
    return c_ans

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
choose = []
ans = 987654321
find(0, 0)
print(ans)