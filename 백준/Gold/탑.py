import sys
sys.stdin = open('탑.txt')

N = int(input())
top = list(map(int, input().split()))
A = []
B = []
ans = []
for i in range(N):
    a = top[i]
    while A:
        if a > A[-1]:
            A.pop()
            B.pop()
        else:
            ans.append(B[-1])
            break
    if not A:
        ans.append(0)
    A.append(a)
    B.append(i+1)
print(*ans)