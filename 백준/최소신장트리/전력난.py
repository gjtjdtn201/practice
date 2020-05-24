import sys
sys.stdin = open('전력난.txt')

import sys
input = sys.stdin.readline
import heapq

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    adj = [[] for _ in range(m)]
    mst = [False]*m
    all_cost = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
        all_cost += c
    q = []
    ans = 0
    heapq.heappush(q, (0, 0))
    while q:
        cost, cur = heapq.heappop(q)
        if mst[cur]:
            continue
        mst[cur] = True
        ans += cost
        for nxt, nxt_cost in adj[cur]:
            if not mst[nxt]:
                heapq.heappush(q, (nxt_cost, nxt))
    print(all_cost-ans)