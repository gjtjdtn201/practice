import sys
sys.stdin = open('별자리 만들기.txt')

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
star = []
adj = [[] for _ in range(n)]
for i in range(n):
    a, b = map(float, input().split())
    star.append((a, b, i))

for i in range(n-1):
    for j in range(i+1, n):
        adj[i].append(((abs(star[i][0]-star[j][0])**2+abs(star[i][1]-star[j][1])**2)**0.5, j))
        adj[j].append(((abs(star[i][0] - star[j][0]) ** 2 + abs(star[i][1] - star[j][1]) ** 2) ** 0.5, i))
mst = [False]*n
q = []
ans = 0
heappush(q, (0, 0))
while q:
    k, cur = heappop(q)
    if mst[cur]:
        continue
    mst[cur] = True
    ans += k
    for cost, nxt in adj[cur]:
        if not mst[nxt]:
            heappush(q, (cost, nxt))
print(ans)