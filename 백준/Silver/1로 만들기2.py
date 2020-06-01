import sys
sys.stdin = open('1로 만들기.txt')

N = int(input())
A = [[] for _ in range(N+1)]
A[1] = [1]
for i in range(2, N+1):
    A[i] = A[i-1] + [i]
    if i%3 == 0 and len(A[i//3])+1 < len(A[i]):
        A[i] = A[i//3] + [i]
    if i%2 == 0 and len(A[i//2])+1 < len(A[i]):
        A[i] = A[i//2] + [i]
print(len(A[-1])-1)
print(*A[-1][::-1])