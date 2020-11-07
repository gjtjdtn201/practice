import sys
sys.stdin = open('최소 신장 트리.txt')

import heapq
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
    mst = [False] * (V + 1)
    q = []
    heapq.heappush(q, (0, 0))
    result = 0
    while q:
        k, node = heapq.heappop(q)
        if mst[node]:
            continue
        mst[node] = True
        result += k
        for dest, weight in graph[node]:
            if not mst[dest]:
                heapq.heappush(q, (weight, dest))

    print('#{} {}'.format(tc, result))