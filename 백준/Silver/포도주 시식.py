import sys
sys.stdin = open('포도주 시식.txt')

N = int(input())
drink = [0]*(N+2)
for i in range(1, N+1):
    drink[i] = int(input())
DP = [0]*(N+2)
DP[1] = drink[1]
DP[2] = drink[1]+drink[2]
for i in range(3, N+1):
    # 첫번째잔, 두번째잔, 못먹는잔
    DP[i] = max(DP[i-2] + drink[i], DP[i-3]+drink[i-1]+drink[i], DP[i-1])
print(DP[N])