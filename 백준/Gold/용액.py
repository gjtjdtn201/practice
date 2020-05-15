N = int(input())
A = list(map(int, input().split()))
A.sort()
lo = 0
hi = N-1
ans = float('inf')
a = b = 0
while lo < hi:
    num = A[hi] + A[lo]
    if num == 0:
        a, b = lo, hi
        break
    if ans > abs(num):
        ans = abs(num)
        a, b = lo, hi
    if num < 0:
        lo += 1
    else:
        hi -= 1
print(A[a], A[b])