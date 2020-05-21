import sys
sys.stdin = open('줄 세우기.txt')

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

tree = [[] for _ in range(N)]
indegree = [0]*N
for i in range(M):
    a, b = map(int, input().split())
    indegree[b-1] += 1
    tree[a-1].append(b-1)

q = deque()
answer = []

for i in range(N):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node+1, end=' ')
    for i in tree[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
