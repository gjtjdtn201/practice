import sys
sys.stdin = open('민석이의 과제 체크하기.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    a = set(range(1, N+1))
    b = set(map(int, input().split()))
    a = a - b

    print('#{} '.format(test_case), end='')
    print(*a)