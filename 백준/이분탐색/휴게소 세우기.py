import sys
sys.stdin = open('휴게소 세우기.txt')

N, M, L = map(int, input().split())

A = list(map(int, input().split()))
A.extend([0, L])
A.sort()
start, end, ans = 0, L, 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        ans = 1
        break
    cnt = 0
    for i in range(1, N+2):
        if A[i] > A[i-1]:
            cnt += (A[i]-(A[i-1]+1))//mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)