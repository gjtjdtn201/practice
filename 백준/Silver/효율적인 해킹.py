import sys
sys.stdin = open('효율적인 해킹.txt', 'r')

def DFS(a):
    global node
    visit = []
    stack = [a]
    while stack:
        n = stack.pop()
        if node[n] != 0:
            node[a] = len(visit) + node[n]
            return node[a]
        for i in tree[n]:
            if i not in visit:
                stack.append(i)
        if n not in visit:
            visit.append(n)
    for k in range(len(visit)):
        node[visit[k]] = len(visit[k:])
    return node[a]

N, M = map(int, input().split())

tree = [[] for i in range(N+1)]
node = [0 for i in range(N+1)]
PA = []
for i in range(M):
    a, b = map(int, input().split())
    PA.append(a)
    tree[b].append(a)
PA = set(range(1, N+1)) - set(PA)

ans = []

if PA == set():
    ans = list(range(1, N+1))

else:
    for i in PA:
        DFS(i)
    for i in range(N):
        if node[i] == max(node):
            ans.append(i)
print(*tuple(ans))