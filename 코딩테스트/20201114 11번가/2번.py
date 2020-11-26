A = [5, 10, 18, 7, 8, 3]
N = len(A)
A.sort(reverse=True)
ans = -1
for i in range(N-2):
    if A[i] < A[i+1]+A[i+2]:
        ans = A[i] + A[i+1] + A[i+2]
        break
print(ans)