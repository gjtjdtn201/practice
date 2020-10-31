import sys
sys.stdin = open('음식배달.txt')

def p(n, s, K, M):
    global ans
    if n == M:
        res = 0
        for i in a:
            res += rest[i][2]
        for ny, nx in house:
            delivery = N*N
            for i in a:
                sy, sx, value = rest[i]
                delivery = min(delivery, (abs(ny-sy)+abs(nx-sx)))
            res += delivery
            if res > ans:
                return
        ans = min(ans, res)
        return
    for i in range(s, K):
        a[n] = i
        p(n+1, i+1, K, M)

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    house = []
    rest = []
    ans = 987654321
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 1:
                house.append((y, x))
            elif matrix[y][x] > 1:
                rest.append((y, x, matrix[y][x]))
    test = len(rest)
    for i in range(1, test+1):
        a = [0] * i
        p(0, 0, test, i)

    print('#{} {}'.format(tc, ans))