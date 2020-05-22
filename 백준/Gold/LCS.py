import sys
sys.stdin = open('LCS.txt')

A = input()
B = input()

arr = [[0]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            arr[j+1][i+1] = arr[j][i]+1
        else:
            arr[j+1][i+1] = max(arr[j][i+1], arr[j+1][i])

print(arr[-1][-1])