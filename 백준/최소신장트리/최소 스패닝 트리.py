import sys
sys.stdin = open('최소 스패닝 트리.txt')

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

V, E = map(int, input().split())

result = []

for _ in range(E):
    node1, node2, cost = map(int, input().split())
    result.append((cost, node1, node2))

result.sort()
cmp = [i for i in range(V+1)]
weight = 0
for cost, node1, node2 in result:
    n1, n2 = find(node1), find(node2)
    if n1 != n2:
        weight += cost
        union(n1, n2)

print(weight)
