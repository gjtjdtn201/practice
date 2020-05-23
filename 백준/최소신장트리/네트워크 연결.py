import sys
sys.stdin = open('네트워크 연결.txt')

import sys
input = sys.stdin.readline

def find(n):
    if n == cmp[n]:
        return n
    cmp[n] = find(cmp[n])
    return cmp[n]

def union(a, b):
    if a < b:
        cmp[b] = a
    else:
        cmp[a] = b

V = int(input())
E = int(input())
result = []

for _ in range(E):
    node1, node2, cost = map(int, input().split())
    result.append((cost, node1, node2))

result.sort()
cmp = [i for i in range(V+1)]
ans = 0
for cost, node1, node2 in result:
    n1, n2 = find(node1), find(node2)
    if n1 != n2:
        ans += cost
        union(n1, n2)
print(ans)