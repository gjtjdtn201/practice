import sys
sys.stdin = open('최소 생산 비용.txt')

def solution(n, k, asum):
    global ans
    if asum > ans:
        return
    if k == n:
        ans = min(asum, ans)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            solution(N, k+1, asum + matrix[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    arr = list(range(N))
    solution(N, 0, 0)
    print('#{} {}'.format(tc, ans))