import sys
sys.stdin = open('K번째 최단경로 찾기.txt')

from heapq import heappush, heappop, heapreplace
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    tree[a-1].append((b-1, c))
ans = [[] for _ in range(n)]
ans[0].append(0)
q = []
heappush(q, (0, 0))
while q:
    cost, cur = heappop(q)
    for nxt, nxt_cost in tree[cur]:
        tmp = cost + nxt_cost
        if len(ans[nxt]) < k:
            heappush(ans[nxt], -tmp)
            heappush(q, (tmp, nxt))
        elif -ans[nxt][0] > tmp:
            heapreplace(ans[nxt], -tmp)
            heappush(q, (tmp, nxt))
for i in ans:
    if len(i) < k:
        print(-1)
    else:
        print(-heappop(i))