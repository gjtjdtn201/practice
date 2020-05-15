from collections import deque

def BFS(i, n):
    visit = [0]*n
    q = deque()
    q.append(i)
    while q:
        a = q.popleft()
        for idx, val in enumerate(matrix[a]):
            if not visit[idx] and val == 1:
                visit[idx] = 1
                q.append(idx)
    return visit

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(' '.join(map(str, BFS(i, N))))