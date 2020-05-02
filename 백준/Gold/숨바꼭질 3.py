import sys
sys.stdin = open('숨바꼭질 3.txt')

from collections import deque

N, K = map(int, input().split())
PG = 100001
dist = [-1]*PG
q = deque()
q.append(N)
dist[N] = 0
while q:
    pos = q.popleft()
    for nxt in [2*pos, pos+1, pos-1]:
        if 0 <= nxt < PG and dist[nxt] == -1:
            if nxt == 2*pos:
                q.appendleft(nxt)
                dist[nxt] = dist[pos]
            else:
                q.append(nxt)
                dist[nxt] = dist[pos]+1

print(dist[K])