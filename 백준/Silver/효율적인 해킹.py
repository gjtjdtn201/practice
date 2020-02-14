import sys
sys.stdin = open('효율적인 해킹.txt', 'r')

def DFS(a):
    visit = [False] * (N + 1)
    visit[a] = True
    stack = [a]
    cnt = 1
    while stack:
        n = stack.pop()
        for i in tree[n]:
            if not visit[i]:
                visit[i] = True
                stack.append(i)
                cnt += 1
    return cnt


N, M = map(int, input().split())

tree = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    tree[b].append(a)
chk = -1
ans = []

for i in range(1, len(tree)):
    c = DFS(i)
    if chk < c:
        chk = c
        ans = [i]
    elif chk == c:
        ans.append(i)

print(*tuple(ans))