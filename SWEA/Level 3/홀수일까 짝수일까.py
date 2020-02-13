import sys
sys.stdin = open('홀수일까 짝수일까.txt','r')

T = int(input())

for test_case in range(1, T+1):
    N = input()
    if int(N[-1]) % 2:
        ans = 'Odd'
    else:
        ans = 'Even'

    print('#{} {}'.format(test_case, ans))