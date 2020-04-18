import sys
# sys.stdin = open('1로 만들기.txt')

A = [0, 0, 1, 1]
N = int(input())
for i in range(4, N+1):
    a = A[i-1]
    if not i%3:
        A.append(min(a, A[i//3])+1)
    elif not i%2:
        A.append(min(a, A[i//2])+1)
    else:
        A.append(a+1)
print(0 if N == 1 else A[-1])