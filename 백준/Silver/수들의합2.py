import sys
sys.stdin = open('수들의합2.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = list(map(int, input().split()))

ans = sum = lo = hi = 0

while True:
    if sum >= M:
        sum -= a[lo]
        lo += 1
    elif hi == N:
        break
    else:
        sum += a[hi]
        hi += 1
    if sum == M:
        ans += 1
print(ans)