import sys
sys.stdin = open('다솔이의 월급 상자.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ans = 0
    for i in range(N):
        p, x = map(float, input().split())
        ans += p*x


    print('#{} {:.6f}'.format(test_case,ans))