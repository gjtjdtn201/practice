import sys
sys.stdin = open('이분그래프.txt', 'r')

from collections import deque

for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    visit = [0]*V
    q = deque()
    for i in range(E):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    chk = 1
    ans = 'YES'
    for k in range(V):
        if chk == 0:
            break
        if not visit[k]:
            visit[k] = 1
            q.append(k)
            while q and chk:
                a = q.popleft()
                for i in graph[a]:
                    if visit[i] == 0:
                        q.append(i)
                        visit[i] = visit[a] * (-1)
                    elif visit[i] + visit[a] != 0:
                        ans = 'NO'
                        chk = 0
                        break
    print(ans)