import sys
sys.stdin = open('촌수계산.txt', 'r')

from collections import deque

n = int(input())
a, b = map(int, input().split())
tree = [[] for _ in range(n)]
visit = [0]*n
visit[a-1] = 1
for i in range(int(input())):
    V, E = map(int, input().split())
    V -= 1
    E -= 1
    tree[V].append(E)
    tree[E].append(V)
q = deque()
q.append(a-1)
ans = -1
while q:
    c = q.popleft()
    if c == b-1:
        ans = visit[b-1]-1
        break
    for i in tree[c]:
        if not visit[i]:
            q.append(i)
            visit[i] = visit[c] + 1
print(ans)
