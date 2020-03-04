import sys
sys.stdin = open('최장경로.txt', 'r')

def dfs(st, cnt):
    global mmax
    if(cnt > mmax):
        mmax = cnt
    for i in range(N+1):
        if(not chk[i] and maplist[st][i] == 1):
            chk[i] = True
            dfs(i, cnt+1)
            chk[i] = False
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    maplist = [[0 for _ in range(N+1)] for _ in range(N+1)]
    mmax = 0
    chk = [False] * (N + 1)
    for _ in range(M):
        st, ed = map(int, input().split())
        maplist[st][ed] = maplist[ed][st] = 1
    for i in range(1, N+1):
        chk[i] = True
        dfs(i, 1)
        chk[i] = False

    print("#{} {}".format(test_case, mmax))