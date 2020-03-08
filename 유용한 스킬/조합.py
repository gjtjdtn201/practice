def f(n, k, s, N):
    if n == k:
        print(C)
    else:
        for i in range(s, N-k+n+1):
            C[n] = i
            f(n+1, k, i+1, N)
N = 5
k = 3
C = [0]*k
f(0, k, 0, N)