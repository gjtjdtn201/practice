import sys
sys.stdin = open("test.txt", "r")

N = int(input())
Ans = list(input())

a = ['A','B','C'] * (N // 2)

b = ['B','A','B','C'] * (N // 2)

c = ['C','C','A','A','B','B'] * (N // 2)


cnt = [0, 0, 0]

for i in range(N):
    if a[i] == Ans[i]:
        cnt[0] += 1
    if b[i] == Ans[i]:
        cnt[1] += 1
    if c[i] == Ans[i]:
         cnt[2] += 1


name = ['Adrian', 'Bruno', 'Goran']

print(max(cnt))
for i in range(3):
    if cnt[i] == max(cnt):
        print(name[i])