import sys
sys.stdin = open('세제곱근을 찾아라.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    i = N**(1/3)

    i = round(i,6)

    if i - round(i) == 0:
        ans = i
    else:
        ans = -1

    print('#{} {}'.format(test_case,round(ans)))