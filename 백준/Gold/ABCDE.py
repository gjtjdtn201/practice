import sys
sys.stdin = open('ABCDE.txt')

import sys
input = sys.stdin.readline

def DFS(n, cnt):
    global chk
    if cnt >= 5:
        chk = True
        return
    visit[n] = True
    for i in tree[n]:
        if not visit[i]:
            DFS(i, cnt+1)
            visit[i] = False

N, M = map(int, input().split())
tree = [[] for _ in range(N)]
visit = [False for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
chk = 0
for i in range(N):
    DFS(i, 1)
    visit[i] = False
    if chk:
        print(1)
        break
else:
    print(0)