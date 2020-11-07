def quick_sort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s - 1)
        quick_sort(a, s + 1, r)

def partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= r and a[i] <= p:
            i += 1
        while j > l and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

a = [1,1,1,1,0,0,0,0,0]
print(a)
quick_sort(a, 0, len(a)-1)
print(a)