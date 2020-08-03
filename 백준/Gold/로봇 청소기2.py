import sys
sys.stdin = open('로봇 청소기2.txt')

from collections import deque
import sys
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def permutation(n):
    global ans, chk2
    if chk2:
        return
    if n == M:
        a = arr[:]
        ans = min(ans, BFS(a))
        if ans == -1:
            chk2 = 1
            return
    for i in range(M):
        if pvisit[i]:
            continue
        arr[n] = task[i]
        pvisit[i] = 1
        permutation(n+1)
        pvisit[i] = 0

def BFS(a):
    global ans
    cnt = 0
    sy, sx = sty, stx
    for my, mx in a:
        if ans <= cnt:
            return cnt
        chk = 0
        q = deque()
        q.append((sy, sx))
        visit = [[0]*w for _ in range(h)]
        visit[sy][sx] = 1
        while q:
            if chk:
                break
            a, b = q.popleft()
            for i in range(4):
                ny = a + dy[i]
                nx = b + dx[i]
                if 0 <= ny < h and 0 <= nx < w and not visit[ny][nx]:
                    if matrix[ny][nx] == '.':
                        if (ny, nx) == (my, mx):
                            cnt += visit[a][b]
                            chk = 1
                            break
                        q.append((ny, nx))
                        visit[ny][nx] = visit[a][b] + 1
        sy, sx = my, mx
        if not chk:
            return -1
    return cnt

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    matrix = [list(input().rstrip()) for _ in range(h)]
    task = []
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == '*':
                task.append((y, x))
                matrix[y][x] = '.'
            elif matrix[y][x] == 'o':
                sty, stx = y, x
                matrix[y][x] = '.'
    if not task:
        print(0)
        continue
    M = len(task)
    ans = float('inf')
    chk2 = 0
    pvisit = [0]*M
    arr = [0]*M
    permutation(0)
    print(ans)
