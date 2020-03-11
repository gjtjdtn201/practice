import sys
sys.stdin = open('러시아 국기 같은 깃발.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    color = []
    for _ in range(N):
        a = list(input())
        w = M - a.count('W')
        b = M - a.count('B')
        r = M - a.count('R')
        color.append((w, b, r))
    ans = 9999999999
    for i in range(1, N-1):
        for j in range(1, i+1):
            res = 0
            bc = j
            rc = N-1-i
            wc = i-bc
            wc += 1
            rc += 1
            for k in range(wc):
                res += color[k][0]
            for k in range(wc, wc + bc):
                res += color[k][1]
            for k in range(wc + bc, N):
                res += color[k][2]
            ans = min(ans, res)

    print('#{} {}'.format(tc, ans))