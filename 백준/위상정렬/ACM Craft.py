import sys
sys.stdin = open('ACM Craft.txt')

import sys
input = sys.stdin.readline
from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    D = list(map(int, input().split()))

    tree = [[] for _ in range(N)]
    indegree = [0]*N
    res = [0]*N
    q = deque()
    cnt = 0

    for i in range(M):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        indegree[b-1] += 1

    end = int(input())

    for i in range(N):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        if node+1 == end:
            print(res[node]+D[node])
            break
        for i in tree[node]:
            res[i] = max(res[i], res[node]+D[node])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)