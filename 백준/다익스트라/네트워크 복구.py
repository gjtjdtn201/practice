import sys
sys.stdin = open('네트워크 복구.txt')

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

cost = {vertex : [float('inf'), 1] for vertex in range(1, N+1)}
cost[1] = [0, 1]
q = []
heappush(q, (0, 1))
while q:
    k, n = heappop(q)
    if k > cost[n][0]:
        continue
    for nxt, nxt_cost in adj[n]:
        tmp = nxt_cost+k
        if tmp < cost[nxt][0]:
            cost[nxt] = [tmp, n]
            heappush(q, (tmp, nxt))
print(len(cost)-1)
for i in range(2, len(cost)+1):
    print(i, cost[i][1])