import sys
sys.stdin = open('연결 요소의 갯수.txt')

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    u, v = find(u), find(v)
    if u != v:
        parent[u] = v
cnt = 0
for i in range(1, N+1):
    if i == find(i):
        cnt += 1
print(cnt)