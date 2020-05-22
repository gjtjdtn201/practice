import sys
sys.stdin = open('전기버스.txt')

def solution(n, k, cnt, energy):
    global ans
    if cnt > ans:
        return
    if k == n:
        ans = min(cnt, ans)
        return
    if energy > 0:
        solution(n, k+1, cnt, energy-1)
    solution(n, k+1, cnt+1, A[k]-1)

for tc in range(1, int(input())+1):
    A = list(map(int, input().split()))
    N = A[0]
    ans = N
    solution(N, 2, 0, A[1]-1)
    print('#{} {}'.format(tc, ans))