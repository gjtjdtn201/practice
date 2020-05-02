import sys
sys.stdin = open('숨바꼭질 3.txt')

from collections import deque

N, K = map(int,input().split())
PG = 100001
dist = [-1]*PG
d = [0]*PG
q = deque()
q.append(N)
dist[N] = 0
d[N] = 1
while q:
    now = q.popleft()
    for nxt in [now+1,now-1,now*2]:
        if 0 <= nxt < PG:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                d[nxt] = d[now]
                q.append(nxt)
            elif dist[nxt] == dist[now]+1:
                d[nxt] += d[now]

print(dist[K])
print(d[K])