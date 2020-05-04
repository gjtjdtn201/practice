import sys
sys.stdin = open('친구 네트워크.txt')

import sys
input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if rank[root1] < rank[root2]:
        rank[root2] += rank[root1]
        parent[root1] = root2
    else:
        rank[root1] += rank[root2]
        parent[root2] = root1


for tc in range(int(input())):
    F = int(input())
    parent = {}
    rank = {}

    for i in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            rank[a] = 1
        if b not in parent:
            parent[b] = b
            rank[b] = 1
        if find(a) != find(b):
            union(a, b)
        print(rank[find(a)])


