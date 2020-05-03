import sys
sys.stdin = open('숨바꼭질 3.txt')

from collections import deque

N, K = map(int, input().split())
PG = 100001
dist = [[-1]*2 for _ in range(PG)]
q = deque()
q.append(N)
dist[N][0] = 0
ans, chk = [K], K
while q:
    pos = q.popleft()
    for nxt in [pos+1, pos-1, pos*2]:
        if 0 <= nxt < PG and dist[nxt][0] == -1:
            q.append(nxt)
            dist[nxt][0] = dist[pos][0]+1
            dist[nxt][1] = pos
while True:
    if dist[chk][1] == -1:
        break
    ans.append(dist[chk][1])
    chk = dist[chk][1]
print(dist[K][0])
print(*reversed(ans))