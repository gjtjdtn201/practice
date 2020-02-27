import sys
sys.stdin = open('장훈이의 높은 선반.txt', 'r')

def powerset(n, k, sum):
    global ans
    if sum >= B:
        if ans > (sum - B):
            ans = sum - B
        return
    if n == k:
        return
    else:
        A[k] = 1
        powerset(n, k + 1, sum + worker[k])
        A[k] = 0
        powerset(n, k + 1, sum)

T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    worker = list(map(int, input().split()))
    A = [0] * N
    ans = 999999
    powerset(N, 0, 0)
    print('#{} {}'.format(test_case, ans))