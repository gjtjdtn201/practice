import sys
sys.stdin = open('수 고르기.txt', 'r')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
hi = lo = 0
ans = 2000000001
a.sort()

while True:
    c = abs(a[hi] - a[lo])
    if c >= M:
        ans = min(ans, c)
    if c <= M and hi < N:
        hi += 1
        if hi == N:
            break
    else:
        lo += 1
print(ans)