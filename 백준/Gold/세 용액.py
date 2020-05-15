N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = float('inf')
a = b = c = 0
chk = 0
for i in range(N-2):
    lo = i+1
    hi = N-1
    while lo < hi:
        num = A[hi] + A[lo] + A[i]
        if num == 0:
            a, b, c = lo, hi, i
            chk = 1
            break
        if ans > abs(num):
            ans = abs(num)
            a, b, c = lo, hi, i
        if num < 0:
            lo += 1
        else:
            hi -= 1
    if chk:
        break
print(A[c], A[a], A[b])