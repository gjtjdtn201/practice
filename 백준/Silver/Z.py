import sys
sys.stdin = open('Z.txt', 'r')

def Z(n, sty, stx, edy, edx):
    global cnt
    if n == 1:
        for y in range(sty, edy):
            for x in range(stx, edx):
                if (y, x) == (r, c):
                    print(cnt)
                    return
                cnt += 1
    else:
        midy = (sty+edy)//2
        midx = (stx+edx)//2
        Z(n-1, sty, stx, midy, midx)
        Z(n-1, sty, midx, midy, edx)
        Z(n-1, midy, stx, edy, midx)
        Z(n-1, midy, midx, edy, edx)

N, r, c = map(int, input().split())
cnt = 0
Z(N,0,0,2**N,2**N)