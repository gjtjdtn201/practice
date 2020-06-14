import sys
sys.stdin = open('유럽여행.txt', 'r')

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, P = map(int, input().split())

c_cost = [0]
minv = 1000
idx = 0
for i in range(1, N+1):
    n = int(input())
    if minv > n:
        minv = n
        idx = i
    c_cost.append(n)

adj = [[] for __ in range(N+1)]
for _ in range(P):
    a, b, c = map(int, input().split())
    adj[a].append((b, c*2+c_cost[a]+c_cost[b]))
    adj[b].append((a, c*2+c_cost[b]+c_cost[a]))

q = []
mst = [False]*(N+1)

heappush(q, (minv, idx))
ans = 0
while q:
    cost, n = heappop(q)
    if mst[n]:
        continue
    mst[n] = True
    ans += cost
    for node, c in adj[n]:
        if not mst[node]:
            heappush(q, (c, node))
print(ans)