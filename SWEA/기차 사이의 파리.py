import sys
sys.stdin = open('기차 사이의 파리.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D / (A+B)
    ans = time * F
    print('#{} {:.10f}'.format(test_case, ans))
