import sys
sys.stdin = open('최소 스패닝 트리.txt')

import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    node1, node2, cost = map(int, input().split())
    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))
pq = []
mst = [False] * (V + 1)
heapq.heappush(pq, (0, 1))
result = 0
while pq:
    k, n = heapq.heappop(pq)
    if mst[n]:
        continue
    mst[n] = True
    result += k
    for node, weight in graph[n]:
        if not mst[node]:
            heapq.heappush(pq, (weight, node))
print(result)