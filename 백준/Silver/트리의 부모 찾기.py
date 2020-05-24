import sys
sys.stdin = open('트리의 부모 찾기.txt')

import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
p = [0]*(N+1)
p[1] = 1
stack = [1]
while stack:
    n = stack.pop()
    for i in tree[n]:
        if p[i] == 0:
            p[i] = n
            stack.append(i)

for i in range(2, N+1):
    print(p[i])