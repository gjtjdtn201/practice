import sys
sys.stdin = open('숨바꼭질 3.txt')

from collections import deque

def find(K):
    q = deque()
    q.append((N, 0))
    while q:
        a, b = q.popleft()
        if 0 <= a < PG and dist[a][b&1] == -1:
            dist[a][b&1] = b
            q.append((a+1, b+1))
            q.append((a-1, b+1))
            q.append((a*2, b+1))
    cnt = 0
    while True:
        K += cnt
        if K >= PG:
            break
        if dist[K][cnt&1] != -1 and dist[K][cnt&1] <= cnt:
            print(cnt)
            return
        cnt += 1
    print(-1)

N, K = map(int, input().split())
PG = 500001
dist = [[-1]*2 for _ in range(PG)]
find(K)