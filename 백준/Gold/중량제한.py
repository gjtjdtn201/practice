import sys
sys.stdin = open('중량제한.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline

def BFS(n):
    q = deque()
    q.append(st)
    visit = [0] * (N + 1)
    visit[st] = 1
    while q:
        a = q.popleft()
        for i, j in tree[a]:
            if not visit[i] and j >= n:
                if i == ed:
                    return True
                q.append(i)
                visit[i] = 1
    return False

def binary(start, end):
    ans = 1
    while start <= end:
        mid = (start+end)//2
        if BFS(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)

N, M = map(int, input().split())

tree = [[] for __ in range(N+1)]
max_wight = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    tree[A].append((B, C))
    tree[B].append((A, C))
    max_wight = max(C, max_wight)
st, ed = map(int, input().split())
binary(1, max_wight)

