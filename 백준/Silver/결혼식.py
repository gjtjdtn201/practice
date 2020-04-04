import sys
sys.stdin = open('결혼식.txt', 'r')

from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(int(input())):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
q = deque()
q.append((1,0))
visit[1] = 1
ans = 0
while q:
    c, cnt = q.popleft()
    if cnt > 1:
        break
    for i in tree[c]:
        if not visit[i]:
            q.append((i, cnt+1))
            ans += 1
            visit[i] = 1
print(ans)

