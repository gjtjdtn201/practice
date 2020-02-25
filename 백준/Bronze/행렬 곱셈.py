import sys
sys.stdin = open('행렬 곱셈.txt', 'r')

N, M = map(int, input().split())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

B = []

for i in range(M):
    B.append(list(map(int, input().split())))

C = [[0 for x in range(K)] for y in range(N)]
for k in range(N):
    for i in range(M):
        for j in range(K):
            C[k][j] += A[k][i] * B[i][j]

for i in C:
    print(*tuple(i))