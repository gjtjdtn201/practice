import sys
sys.stdin = open('최단경로.txt')

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
        if dist[c_v][0] > c_dist:
            continue
        for adj, weight in graph[c_v].items():
            d = c_dist + weight
            if d < dist[adj][0]:
                dist[adj] = [d, c_v]
                heapq.heappush(q, [d, adj])

    for i,j in dist.items():
        print('INF' if j[0] == float('inf') else j[0])

V, E = map(int, input().split())

K = input().rstrip()

mygraph = {str(i): {} for i in range(1, V+1)}

for _ in range(E):
    a, b, c = input().rstrip().split()
    if b in mygraph[a]:
        if mygraph[a][b] > int(c):
            mygraph[a][b] = int(c)
    else:
        mygraph[a][b] = int(c)

DSR(mygraph, K)