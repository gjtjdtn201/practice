import sys
sys.stdin = open('아기상어.txt', 'r')

from collections import deque

def bfs(maplist, q):
    size, eat_cnt = 2, 0
    mmin = 0
    chk = [[False for _ in range(N)] for _ in range(N)]
    while(q):
        dist, y, x = q.popleft()
        if(0 < maplist[y][x] < size):
            eat_cnt += 1
            maplist[y][x] = 0
            if(eat_cnt == size):
                size += 1
                eat_cnt = 0
            mmin += dist
            dist = 0
            q = deque()
            chk = [[False for _ in range(N)] for _ in range(N)]
        for i in range(4):
            new_dist = dist + 1
            sty = y + dy[i]
            stx = x + dx[i]
            if(0 <= sty < N and 0 <= stx < N and not chk[sty][stx] and maplist[sty][stx] <= size):
                chk[sty][stx] = True
                q.append((new_dist, sty, stx))
        q = deque(sorted(q))
    return mmin
N = int(input())
maplist = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for y in range(N):
    for x in range(N):
        if(maplist[y][x] == 9):
            q.append((0, y, x))
            maplist[y][x] = 0
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
result = bfs(maplist, q)
print(result)
