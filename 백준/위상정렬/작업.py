import sys
sys.stdin = open('작업.txt')

from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
time = [0]
for i in range(1, N+1):
    A = list(map(int, input().split()))
    time.append(A[0])
    for j in range(2, len(A)):
        tree[A[j]].append(i)
        indegree[i] += 1

q = deque()
ans = [0]*(N+1)
for i in range(N+1):
    ans[i] += time[i]
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    for i in tree[node]:
        indegree[i] -= 1
        ans[i] = max(ans[i], ans[node]+time[i])
        if indegree[i] == 0:
            q.append(i)

print(max(ans))
