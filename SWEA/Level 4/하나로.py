import sys
sys.stdin = open('하나로.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    dist = [[0]*N for _ in range(N)]
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    for i in range(N-1):
        for j in range(i+1, N):
            cost = (x[i]-x[j])**2 + (y[i]-y[j])**2
            dist[i][j] = dist[j][i] = cost
    PI = list(range(N))
    ans = 0
    u = 0
    D = [float('inf')]*N
    D[u] = 0
    visit = [False]*N
    for i in range(N):
        minv = float('inf')
        for v in range(N):
            if not visit[v] and minv > D[v]:
                minv = D[v]
                u = v
        visit[u] = True
        ans += dist[PI[u]][u]*E
        for v in range(N):
            if not visit[v] and dist[u][v] < D[v]:
                D[v] = dist[u][v]
                PI[v] = u

    print('#{} {}'.format(tc, round(ans)))
