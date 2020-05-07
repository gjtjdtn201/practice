import sys
sys.stdin = open('환승.txt', 'r')

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    q = deque()
    q.append(1)
    visit[1] = 1
    while q:
        a = q.popleft()
        if a == N:
            print(visit[a])
            return
        for nx in matrix[a]:
            if not visit[nx]:
                if nx == N:
                    print(visit[a]+1)
                    return
                if nx >= N:
                    visit[nx] = visit[a]
                    q.append(nx)
                else:
                    visit[nx] = visit[a] + 1
                    q.append(nx)
    print(-1)

N, K, M = map(int, input().split())
matrix = [[] for _ in range(N+M+1)]
visit = [0 for _ in range(N+M+1)]

for i in range(M):
    row = list(map(int, input().split()))
    for j in range(K):
        matrix[row[j]].append(N+i+1)
        matrix[N+i+1].append(row[j])

BFS()