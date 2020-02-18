def permutation(n, k):
    if k == n:
        b = arr[:]
        a.append(b)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]
arr = [0,1,2]
n = 3
k = 0
a = []
permutation(n, k)
print(a)