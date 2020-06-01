import sys
sys.stdin = open('RGB 거리.txt')

N = int(input())
R, G, B = [0], [0], [0]
DP = [[0]*3 for _ in range(N+1)]
for i in range(N):
    a, b, c = map(int, input().split())
    R.append(a)
    G.append(b)
    B.append(c)
for i in range(1, N+1):
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + R[i]
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + G[i]
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + B[i]
print(min(DP[N]))