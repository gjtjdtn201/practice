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
    ans = N * M
    # i는 흰색과 파란색의 구분
    for i in range(1, N-1):
        # j는 파란색과 빨간색의 구분
        for j in range(i, N-1):
            cnt = 0
            for k in range(i):
                cnt += color[k][0]
            for k in range(i,j+1):
                cnt += color[k][1]
            for k in range(j+1, N):
                cnt += color[k][2]
            ans = min(cnt, ans)

    print('#{} {}'.format(tc, ans))