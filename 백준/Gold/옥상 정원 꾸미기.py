import sys
sys.stdin = open('옥상 정원 꾸미기.txt', 'r')

N = int(input())
A = []
ans = 0
for i in range(N):
    a = int(input())
    while A:
        if A[-1] <= a:
            A.pop()
        else:
            break
    A.append(a)
    ans += len(A)-1

print(ans)