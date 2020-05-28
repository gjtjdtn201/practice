import sys
sys.stdin = open('행성 터널.txt')

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
star = []
for i in range(N):
    x, y, z = map(int, input().split())
    star.append((x, y, z, i))
edges = [[] for _ in range(N)]
for i in range(3):
    star.sort(key=lambda x: x[i])
    for j in range(N-1):
        n1, n2 = star[j][3], star[j+1][3]
        cost = abs(star[j][i]-star[j+1][i])
        edges[n1].append((cost, n2))
        edges[n2].append((cost, n1))

mst = [False]*N
ans = 0
q = []
heappush(q, (0, 0))

while q:
    cost, node = heappop(q)
    if mst[node]:
        continue
    ans += cost
    mst[node] = True
    for nxt_cost, nxt in edges[node]:
        if mst[nxt]:
            continue
        heappush(q, (nxt_cost, nxt))

print(ans)