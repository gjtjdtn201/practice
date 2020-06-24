import sys
sys.stdin = open('파괴된 도시.txt')

import sys
input = sys.stdin.readline

def DFS(chk, idx, chk2):
    global ans, res, chk3
    if chk3:
        return
    if len(chk) > K:
        return
    if len(chk) == K:
        ans2 = set(chk)
        if ans2 == broken:
            ans = len(chk2)
            res = chk2[:]
            chk3 = 1
        return
    for i in range(idx, N+1):
        if not visit[i]:
            cnt = 1
            chk2 += [i]
            chk += [i]
            visit[i] = 1
            for node in adj[i]:
                if not visit[node]:
                    cnt += 1
                    chk += [node]
                    visit[node] = 1
            DFS(chk, i, chk2)
            for j in range(cnt):
                a = chk.pop()
                visit[a] = 0
            chk2.pop()

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

K = int(input())

broken = set(map(int, input().split()))
visit = [0]*(N+1)
ans, chk3 = -1, 0
res = []
DFS([], 1, [])
print(ans)
if ans != -1:
    print(*res)