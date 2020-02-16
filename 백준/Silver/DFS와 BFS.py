import sys
sys.stdin = open('DFS와 BFS.txt', 'r')

from collections import deque

def DFS(val):
    stack = [val]
    visit = []
    while stack:
        n = stack.pop()
        tree[n].sort(reverse=True)
        for i in tree[n]:
            if i not in visit:
                stack.append(i)
        if n not in visit:
            visit.append(n)
    return visit

def BFS(val):
    queue = deque()
    queue.append(val)
    visit = [val]
    while queue:
        n = queue.popleft()
        tree[n].sort()
        for i in tree[n]:
            if i not in visit:
                queue.append(i)
                visit.append(i)
    return visit

N, M, V = map(int, input().split())
tree = [[] for num in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(*tuple(DFS(V)))
print(*tuple(BFS(V)))