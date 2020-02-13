import sys
sys.stdin = open('바이러스.txt', 'r')

def DFS(a):
    stack = [a]
    visit = []
    while stack:
        n = stack.pop()
        for i in tree[n]:
            if i not in visit:
                stack.append(i)
        if n not in visit:
            visit.append(n)
    return visit

T = int(input())

N = int(input())

tree = [[] for n in range(T+1)]
for i in range(N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(len(DFS(1))-1)