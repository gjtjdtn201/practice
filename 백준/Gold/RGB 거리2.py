import sys
sys.stdin = open('RGB 거리2.txt')

N = int(input())
A = []
ans = float('inf')
for i in range(N):
    A.append((list(map(int, input().split()))))
for i in range(3):
    DP = [[0] * 3 for _ in range(N)]
    for j in range(3):
        if i == j:
            DP[0][j] = A[0][i]
        else:
            DP[0][j] = float('inf')
    for k in range(1, N):
        DP[k][0] = A[k][0] + min(DP[k - 1][1], DP[k - 1][2])
        DP[k][1] = A[k][1] + min(DP[k - 1][0], DP[k - 1][2])
        DP[k][2] = A[k][2] + min(DP[k - 1][0], DP[k - 1][1])

    for l in range(3):
        if i != l:
            ans = min(ans, DP[-1][l])
print(ans)


