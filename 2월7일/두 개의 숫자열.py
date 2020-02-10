import sys
sys.stdin = open('두 개의 숫자열.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A
    ans = 0
    for i in range(M-N+1):
        cnt = 0
        for j in range(N):
            cnt += A[j]*B[i+j]
        if ans < cnt:
            ans = cnt


    print('#{} {}'.format(test_case, ans))