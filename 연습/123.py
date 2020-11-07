import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B = int(input())

tree = [[] for _ in range(N)]
start = []
for i in range(len(A)):
    if A[i] == -1:
        start.append(i)
        continue
    tree[A[i]].append(i)
ans = 0
for j in start:
    stack = [j]
    while stack:
        a = stack.pop()
        if a == B:
            continue
        if tree[a] == [B]:
            ans += 1
        elif tree[a]:
            for i in tree[a]:
                stack.append(i)
        else:
            ans += 1

print(ans)