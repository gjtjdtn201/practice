import sys
sys.stdin = open('새샘이의 7-3-5 게임.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    ml = list(map(int,input().split()))
    a = set([i+j+k for i in ml for j in ml for k in ml if i < j and j < k])
    b = sorted(a, reverse=True)

    print('#{} {}'.format(test_case, b[4]))