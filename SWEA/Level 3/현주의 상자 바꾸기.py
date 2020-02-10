import sys
sys.stdin = open('현주의 상자 바꾸기.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())

    a = [0]*N

    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            a[j] = i

    a = tuple(a)
    print('#{} '.format(test_case),end='')
    print(*a)