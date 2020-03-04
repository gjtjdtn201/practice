import sys
sys.stdin = open('동철이의 일 분배.txt', 'r')

def per(n, k, asum):
    global ans
    if n == k:
        ans = max(ans, asum)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            if asum * P[k][arr[k]] * 0.01 > ans:
                per(n, k + 1, asum * P[k][arr[k]]*0.01)
            arr[k], arr[i] = arr[i], arr[k]

for tc in range(1, int(input())+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    arr = list(range(N))
    per(N, 0, 100)
    print('#{} {:.6f}'.format(tc, ans))