import sys
sys.stdin = open('개똥벌레.txt', 'r')

N, H = map(int, input().split())
A = [0]*(H+1)
B = [0]*(H+1)
T = [0]*(H+1)
TA = [0]*(H+1)
TB = [0]*(H+1)
for i in range(N):
    k = int(input())
    if i%2:
        A[k] += 1
    else:
        B[k] += 1
ans = 1
chk = 987654321
for i in range(H-1, 0, -1):
    TB[i] = B[i] + TB[i+1]
    TA[i] = A[i] + TA[i+1]

for i in range(1, H+1):
    T[i] = TB[i] + TA[H-i+1]
    if T[i] < chk:
        chk = T[i]
        ans = 1
    elif T[i] == chk:
        ans += 1
print(chk, ans)