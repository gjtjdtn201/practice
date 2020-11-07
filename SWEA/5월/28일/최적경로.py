import sys
sys.stdin = open('최적경로.txt')

def DFS(nx, ny, cnt, asum):
    global ans
    if asum >= ans:
        return
    if cnt == N:
        asum += abs(nx - home[0]) + abs(ny - home[1])
        ans = min(asum, ans)
        return
    for i in range(N):
        if not chk[i]:
            chk[i] = 1
            tmp = abs(nx - location[i][0]) + abs(ny - location[i][1])
            DFS(location[i][0], location[i][1], cnt + 1, asum + tmp)
            chk[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    a = list(map(int, input().split()))
    location, home = [], []
    home.extend((a[2], a[3]))
    for i in range(4, len(a) - 1, 2):
        location.append((a[i], a[i + 1]))
    ans = float('inf')
    chk = [0] * N
    DFS(a[0], a[1], 0, 0)

    print('#{} {}'.format(tc, ans))