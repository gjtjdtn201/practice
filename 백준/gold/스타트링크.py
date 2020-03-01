import sys
sys.stdin = open('스타트링크.txt', 'r')

from collections import deque

# 총건물, 현재위치, 목적지, 오름, 내림
F, S, G, U, D = map(int, input().split())
F -= 1
S -= 1
G -= 1
visit = [0] * (F+1)
queue = deque()
queue.append(S)
ans = 'use the stairs'

dx = [U, -D]

while queue:
    pos = queue.popleft()
    if pos == G:
        ans = visit[pos]
        break
    for i in range(2):
        nextpos = pos + dx[i]
        if F >= nextpos >= 0 and not visit[nextpos] and nextpos != S:
            visit[nextpos] = visit[pos] + 1
            queue.append(nextpos)
print(ans)