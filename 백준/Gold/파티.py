import sys
sys.stdin = open('파티.txt')

import heapq
import sys
input = sys.stdin.readline

def DSR(graph, start):
    dist = {v:[float('inf'), start] for v in graph}
    dist[start] = [0, start]
    q = []
    heapq.heappush(q, [dist[start][0], start])
    while q:
        c_dist, c_v = heapq.heappop(q)
        if dist[c_v][0] < c_dist:
            continue
        for adj, weight in graph[c_v].items():
            d = c_dist + weight
            if d < dist[adj][0]:
                dist[adj] = [d, c_v]
                heapq.heappush(q, [d, adj])

    for i, j in dist.items():
        ans[int(i)] += j[0]

N, M, X = map(int, input().split())

graph1 = {str(i): {} for i in range(1, N+1)}
graph2 = {str(i): {} for i in range(1, N+1)}

for i in range(M):
    a, b, c = input().strip().split()
    graph1[a][b] = int(c)
    graph2[b][a] = int(c)

ans = [0]*(N+1)

DSR(graph1, str(X))
DSR(graph2, str(X))

print(max(ans))