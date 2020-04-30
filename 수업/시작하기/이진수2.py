import sys
sys.stdin = open('이진수2.txt')

for tc in range(1, int(input())+1):
    ans = ''
    N = float(input())
    chk = 0
    for i in range(12):
        N = 2 * N
        if N >= 1:
            N -= 1
            ans += '1'
        else:
            ans += '0'
        if N == 0:
            chk = 1
            break
    print('#{} {}'.format(tc, ans if chk else 'overflow'))