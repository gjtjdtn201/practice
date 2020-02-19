import sys
sys.stdin = open('테트로미노.txt', 'r')

N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

# 1.네모 2. 눕힌 3개에서 돌리면서 7개탐색, 3. 세로 3개에서 7개 탐색
ans = 0
for y in range(N-1):
    for x in range(M-1):
        cnt = 0
        for z in range(2):
            cnt += matrix[y+z][x] + matrix[y+z][x+1]
        if cnt > ans:
            ans = cnt

dy = [-1,-1,-1,0,1,1,1]
dx = [0,1,2,3,2,1,0]

for y in range(N):
    for x in range(M-2):
        for z in range(7):
            cnt = 0
            ny = y + dy[z]
            nx = x + dx[z]
            if 0 <= ny < N and 0 <= nx < M:
                cnt = matrix[y][x] + matrix[y][x+1] + matrix[y][x+2] + matrix[ny][nx]
            else:
                continue
            if cnt > ans:
                ans = cnt

for y in range(N-2):
    for x in range(M):
        for z in range(7):
            cnt = 0
            ny = y + dx[z]
            nx = x + dy[z]
            if 0 <= ny < N and 0 <= nx < M:
                cnt = matrix[y][x] + matrix[y+1][x] + matrix[y+2][x] + matrix[ny][nx]
            else:
                continue
            if cnt > ans:
                ans = cnt

print(ans)