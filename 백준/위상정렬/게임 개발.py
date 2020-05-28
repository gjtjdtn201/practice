import sys
sys.stdin = open('게임 개발.txt')

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
tree = [[] for _ in range(N)]
indegree = [0]*N
build = []
for i in range(N):
    a = list(map(int, input().split()))
    build.append(a[0])
    for j in range(1, len(a)-1):
        tree[a[j]-1].append(i)
        indegree[i] += 1

q = deque()
ans = [0]*N
for i in range(N):
    ans[i] += build[i]
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    for i in tree[node]:
        indegree[i] -= 1
        ans[i] = max(ans[i], ans[node]+build[i])
        if indegree[i] == 0:
            q.append(i)
for i in ans:
    print(i)