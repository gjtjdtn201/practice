import sys
sys.stdin = open('컨테이너 운반.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort()
    ans = 0
    for i in range(M):
        for j in range(N):
            if W[j] == 0:
                continue
            if W[j] <= T[i]:
                ans += W[j]
                W[j] = 0
                break
    print('#{} {}'.format(tc, ans))