import sys
sys.stdin = open('행성 터널.txt')

import sys
input = sys.stdin.readline

def find(a):
    if a == cmp[a]:
        return a
    cmp[a] = find(cmp[a])
    return cmp[a]

def union(a, b):
    if a < b:
        cmp[b] = a
    else:
        cmp[a] = b

N = int(input())
star = []
for i in range(N):
    x, y, z = map(int, input().split())
    star.append((x, y, z, i))
res = []
for i in range(3):
    star.sort(key=lambda x: x[i])
    cur = star[0][3]
    for j in range(1, N):
        nxt = star[j][3]
        res.append((abs(star[j][i]-star[j-1][i]), cur, nxt))
        cur = nxt
cmp = [i for i in range(N)]
ans = 0
res.sort()
for cost, node1, node2 in res:
    n1, n2 = find(node1), find(node2)
    if n1 != n2:
        ans += cost
        union(n1, n2)
print(ans)