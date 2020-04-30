import sys
sys.stdin = open('이진수.txt')

for tc in range(1, int(input())+1):
    N, M = map(str, input().split())
    M = '0x' + M
    dec = int(M, 16)
    ans = bin(dec)
    length = (int(N)*4) - (len(ans)-2)
    result = '0'*length + ans[2:]
    print('#{} {}'.format(tc, result))
