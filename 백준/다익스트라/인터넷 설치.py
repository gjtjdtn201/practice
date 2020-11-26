import sys
sys.stdin = open('인터넷 설치.txt')

def DFS(a,b,c,d):
    global ans
    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5 and (ny, nx) not in d:
            if ord(board[a][b]) < ord(board[ny][nx]) and visit[ny][nx][c] < visit[a][b][c]:
                visit[ny][nx][c] = visit[a][b][c] + 1
                ans = max(ans, visit[ny][nx][c])
                d.append((ny,nx))
                DFS(ny, nx, c, d)
                d.pop()
            elif ord(board[a][b]) >= ord(board[ny][nx]) and c == 0 and visit[ny][nx][c + 1] < visit[a][b][c]:
                visit[ny][nx][c + 1] = visit[a][b][c] + 1
                ans = max(ans, visit[ny][nx][c + 1])
                d.append((ny,nx))
                DFS(ny, nx, c+1, d)
                d.pop()

board = [list(input()) for _ in range(5)]

visit = [[[0, 0] for _ in range(5)] for __ in range(5)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ans = 0
chk = 0
for y in range(5):
    for x in range(5):
        if visit[y][x][0] == 0:
            visit[y][x][0] = 1
            DFS(y, x, 0, [(y,x)])
for i in visit:
    print(i)
print(ans)