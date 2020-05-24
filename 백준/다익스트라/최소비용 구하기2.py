import sys
sys.stdin = open('최소비용 구하기2.txt')

import heapq
import sys
input = sys.stdin.readline

def DSR(start, end):
    distances = {vertex : [float('inf'), start] for vertex in range(1, N+1)}
    distances[start] = [0, start]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cur_cost, cur = heapq.heappop(q)
        if cur_cost > distances[cur][0]:
            continue
        for nxt, nxt_cost in adj[cur]:
            tmp = cur_cost + nxt_cost
            if tmp < distances[nxt][0]:
                distances[nxt] = [tmp, cur]
                heapq.heappush(q, (tmp, nxt))
    print(distances[end][0])
    cities = [end]
    path = end
    while distances[path][1] != start:
        cities.append(distances[path][1])
        path = distances[path][1]
    cities.append(start)
    print(len(cities))
    print(*cities[::-1])

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
start, end = map(int, input().split())
DSR(start, end)