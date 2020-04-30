import sys
sys.stdin = open('부분합.txt')

N, M = map(int, input().split())

a = list(map(int, input().split()))

sum = lo = hi = 0
ans = 100001

while True:
    if sum >= M:
        sum -= a[lo]
        lo += 1
    elif hi == N:
        break
    else:
        sum += a[hi]
        hi += 1
    if sum >= M:
        ans = min(ans, hi-lo)
print(0 if ans == 100001 else ans)