import sys
sys.stdin = open('최소 이동 거리.txt')

import heapq
def DSR(start, end):
    cost = [float('inf')] *(N+1)
    q = []
    cost[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cur_cost, cur = heapq.heappop(q)
        if cur_cost > cost[cur]:
            continue
        for nxt, nxt_cost in adj[cur]:
            tmp = cost[cur] + nxt_cost
            if tmp < cost[nxt]:
                cost[nxt] = tmp
                heapq.heappush(q, (tmp, nxt))

    return cost[end]

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for i in range(E):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
    print('#{} {}'.format(tc, DSR(0, N)))