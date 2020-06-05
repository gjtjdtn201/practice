import sys
sys.stdin = open('친구비.txt')

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


N, M, k = map(int, input().split())

money = list(map(int, input().split()))

p = [i for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    n1, n2 = find(a-1), find(b-1)
    if n1 != n2:
        if money[n1] < money[n2]:
            p[n2] = n1
        else:
            p[n1] = n2
ans = 0
for i in range(N):
    friend = find(p[i])
    if friend == i:
        ans += money[i]
        if ans > k:
            print('Oh no')
            break
else:
    print(ans)