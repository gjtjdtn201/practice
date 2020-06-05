import sys
sys.stdin = open('집배원 한상덕.txt')

from collections import deque
import sys
input = sys.stdin.readline

def BFS(lo, hi):
    visit = [[0] * N for _ in range(N)]
    q = deque()
    q.append((house[0][0], house[0][1]))
    visit[house[0][0]][house[0][1]] = 1
    while q:
        a, b = q.popleft()
        for i in range(8):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
                if lo <= level[ny][nx] <= hi:
                    q.append((ny, nx))
                    visit[ny][nx] = 1
    for y, x in house:
        if visit[y][x] == 0:
            return False
    return True

N = int(input())

matrix, house = [], []
for i in range(N):
    a = list(input().rstrip())
    matrix.append(a)
    for j, k in enumerate(a):
        if k == 'P' or k == 'K':
            house.append([i, j])

level, pointerset = [], set()

for i in range(N):
    A = list(map(int, input().split()))
    level.append(A)
    pointerset.update(A)
pointer = sorted(list(pointerset))
lmin = pointer[0]
rmax = pointer[-1]

lmax, rmin = float('inf'), 0
for y, x in house:
    lmax = min(lmax, level[y][x])
    rmin = max(rmin, level[y][x])
lolist, hilist = [], []
for i in pointer:
    if lmin <= i <= lmax:
        lolist.append(i)
    if rmin <= i <= rmax:
        hilist.append(i)

ans = float('inf')
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

i, j = 0, 0
while i < len(lolist) and j < len(hilist):
    lchk, rchk = 0, 0
    if BFS(lolist[i], hilist[j]):
        ans = min(ans, hilist[j] - lolist[i])
        i += 1
        lchk = 1
    else:
        j += 1
        rchk = 1
print(ans)