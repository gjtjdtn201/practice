import sys
sys.stdin = open('음악프로그램.txt')

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

tree = [[] for _ in range(N)]
indegree = [0]*N
q = deque()
answer = []

for i in range(M):
    a = list(map(int, input().split()))
    for i in range(1, len(a)-1):
        tree[a[i]-1].append(a[i+1]-1)
        indegree[a[i+1]-1] += 1

for i in range(N):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    answer.append(node+1)
    for i in tree[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(answer) != N:
    print(0)
else:
    for i in answer:
        print(i)