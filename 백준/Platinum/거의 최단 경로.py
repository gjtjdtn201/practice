import sys
sys.stdin = open('거의 최단 경로.txt')

from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = 987654321

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    tree = [[0]*N for _ in range(N)]

    S, D = map(int, input().split())
    for i in range(M):
        U, V, P = map(int, input().split())
        tree[U][V] = P

    ans = 0
    while True:
        cost = [INF] * N
        q = []
        heappush(q, (0, S))
        cost[S] = 0
        while q:
            cur_cost, cur = heappop(q)
            if cur_cost > cost[cur]:
                continue
            for i in range(N):
                if tree[cur][i] and cost[i] > cur_cost + tree[cur][i]:
                    cost[i] = cur_cost + tree[cur][i]
                    heappush(q, (cost[i], i))

        cnt = cost[D]

        if cnt == 987654321:
            print(-1)
            break

        if cnt != ans and ans != 0:
            if cnt == 987654321:
                print(-1)
            else:
                print(cnt)
            break
        ans = cnt

        qu = deque()
        qu.append(D)
        while qu:
            num = qu.popleft()
            for i in range(N):
                if tree[i][num] and cost[i] + tree[i][num] == cost[num]:
                    tree[i][num] = 0
                    qu.append(i)