import sys
sys.stdin = open('도시 분할 계획.txt')

import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

ans = 0
mst = [False]*(N+1)
maxv = 0
q = []
heapq.heappush(q, (0, 1))
while q:
    k, n = heapq.heappop(q)
    if mst[n]:
        continue
    mst[n] = True
    maxv = max(k, maxv)
    ans += k
    for node, wt in adj[n]:
        if not mst[node]:
            heapq.heappush(q, (wt, node))
print(ans-maxv)