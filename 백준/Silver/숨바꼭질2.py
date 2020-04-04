import sys
sys.stdin = open('숨바꼭질2.txt', 'r')

from collections import deque

N, M = map(int, input().split())

tree = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for i in range(M):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

q = deque()
q.append(1)
visit[1] = 1
ans1 = N+1
ans2 = 0
ans3 = 1
while q:
    a = q.popleft()
    for i in tree[a]:
        if not visit[i]:
            q.append(i)
            visit[i] = visit[a] + 1
            if ans2 < visit[i]:
                ans2 = visit[i]
                ans3 = 1
                ans1 = i
            elif ans2 == visit[i]:
                ans3 += 1
                if ans1 > i:
                    ans1 = i
print(ans1, ans2-1, ans3)