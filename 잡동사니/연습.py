def printSet(n):
    sum = 0
    for i in range(n):
        if A[i] == 1:
            sum += data[i]

    if sum == 10:
        a = []
        for i in range(n):
            if A[i] == 1:
                a.append(data[i])
        s.append(a)

def powerset(n, k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

N = 10
A = [0 for _ in range(N)]  # 원소의 포함여부 저장 (0, 1)
data = list(range(1,11))
s = []
powerset(N, 0)
print(s)