import sys
sys.stdin = open('진수의 홀수 약수.txt', 'r')

Maxval = 10**6 + 1
DP = [0] * Maxval
for i in range(1, Maxval, 2):
    for j in range(i, Maxval, i):
        DP[j] += i

for i in range(1, Maxval):
    DP[i] += DP[i - 1]

T = int(input())

for test_case in range(1, T+1):
    L, R = map(int, input().split())
    ans = DP[R] - DP[L - 1]

    print('#{} {}'.format(test_case, ans))