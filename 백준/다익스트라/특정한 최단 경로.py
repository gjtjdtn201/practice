import sys
sys.stdin = open('특정한 최단 경로.txt')

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def DSR(start):
    q = []
    cost = [float('inf')] * N
    heappush(q, (0, start))
    cost[start] = 0
    while q:
        cur_cost, cur = heappop(q)
        if cur_cost > cost[cur]:
            continue
        for nxt, nxt_cost in tree[cur]:
            tmp = cur_cost + nxt_cost
            if tmp < cost[nxt]:
                cost[nxt] = tmp
                heappush(q, (tmp, nxt))
    return cost

N, E = map(int, input().split())
tree = [[] for _ in range(N)]

for i in range(E):
    a, b, c = map(int, input().split())
    tree[a-1].append((b-1, c))
    tree[b-1].append((a-1, c))

v1, v2 = map(int, input().split())
A1 = DSR(0)
A2 = DSR(v1-1)
A3 = DSR(v2-1)
ans = min(A1[v1-1]+A2[v2-1]+A3[N-1], A1[v2-1]+A3[v1-1]+A2[N-1])
print(-1 if ans == float('inf') else ans)
