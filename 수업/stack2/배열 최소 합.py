import sys
sys.stdin = open("배열 최소 합.txt", "r")

def permutation(n, k, asum):
    global ans
    if asum > ans:
        return
    if k == n:
        if asum < ans:
            ans = asum
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(n, k + 1, asum + matrix[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    ans = 9999
    arr = list(range(N))
    permutation(N, 0, 0)

    print('#{} {}'.format(test_case, ans))