import sys
sys.stdin = open('감시.txt', 'r')

def solution(n):
    global ans
    if n == C:
        cnt = 0
        # count 함수는 엄청 느리니까 쓰지말자..
        for y in range(N):
            for x in range(M):
                if matrix[y][x] == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return
    a, b, c = cctv[n]
    for i in check[c]:
        watch = []
        for j in i:
            ny, nx = a, b
            while 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] != 6:
                if matrix[ny][nx] == 0:
                    watch.append((ny, nx))
                    matrix[ny][nx] = -1
                ny += dy[j]
                nx += dx[j]
        solution(n+1)
        for k in watch:
            matrix[k[0]][k[1]] = 0

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

check = [[[0],[1],[2],[3]],
        [[0,2],[1,3]],
        [[0,1],[1,2],[2,3],[3,0]],
        [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
        [[0,1,2,3]]]

cctv = []
for y in range(N):
    for x in range(M):
        if 0 < matrix[y][x] < 6:
            cctv.append((y, x, matrix[y][x]-1))

C = len(cctv)
ans = N*M

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
solution(0)
print(ans)