import sys
sys.stdin = open('Two Dots.txt')

def DFS(i, j, k):
    q = []
    q.append((i, j, 1))
    while q:
        a, b, c = q.pop()
        visit[a][b] = c
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == k:
                if visit[ny][nx] != 0:
                    if visit[ny][nx]+2 <= visit[a][b]:
                        return True
                else:
                    q.append((ny, nx, c+1))
    return False

N, M = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(N)]
visit = [[0]*M for __ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

ans = False
for y in range(N):
    if ans:
        break
    for x in range(M):
        if visit[y][x] == 0:
            edy, edx = y, x
            ans = DFS(y, x, matrix[y][x])
            if ans:
                break
print('Yes' if ans else 'No')
#DFS 로 풀자