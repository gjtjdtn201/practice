import sys
sys.stdin = open('숨바꼭질.txt', 'r')

from collections import deque

def find():
    global chk
    while queue:
        pos = queue.popleft()
        if pos == K:
            chk = 1
            return visit[pos]
        nextpos(pos -1, pos)
        nextpos(pos +1, pos)
        nextpos(pos * 2, pos)

def nextpos(next, pos):
    global chk
    if chk == 1:
        return
    if PG > next >= 0 and (visit[next] == 0 or visit[pos] + 1 < visit[next]):
        visit[next] = visit[pos] + 1
        queue.append(next)

N, K = map(int, input().split())
queue = deque()
queue.append(N)
PG = 100001
chk = 0
visit = [0] * PG
print(find())