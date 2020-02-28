def permutation(n, k):
    if k == n:
        b = arr[:]
        a.append(b)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]
arr = [1, 1, 2, 3]
n = 4
k = 0
a = []
permutation(n, k)
print(a)
print(len(a))