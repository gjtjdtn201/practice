M = int(input())
if M == 0:
    print(0)
else:
    mod = 1000000
    N = M%(15*(10**5))
    A = [0]*(N+1)
    A[0], A[1] = 0, 1
    for i in range(2, N+1):
        A[i] = A[i-1] + A[i-2]
        A[i] %= mod
    print(A[N])