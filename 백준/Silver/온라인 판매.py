import sys
sys.stdin = open('온라인 판매.txt')

N, M = map(int, input().split())

cus = []
for i in range(M):
    cus.append(int(input()))
cus.sort(reverse=True)
cnt, cnt2 = 0, 0
for i in range(1, M+1):
    if i > N:
        break
    if cus[i-1]*i > cnt:
        cnt = cus[i-1]*i
        cnt2 = cus[i-1]

print(cnt2, cnt)

