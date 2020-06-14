import sys
sys.stdin = open('일요일 아침의 데이트.txt')

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def start():
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 'S':
                return y, x

def BFS(sty, stx):
    q = []
    heappush(q, (10000, sty, stx))
    visit = [[0]*M for __ in range(N)]
    visit[sty][stx] = 1
    while q:
        c, a, b = heappop(q)
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
                if matrix[ny][nx] == 'g':
                    heappush(q, (c+10000, ny, nx))
                    visit[ny][nx] = 1
                elif matrix[ny][nx] == 'F':
                    print(c//10000-1, c%10000)
                    return
                else:
                    chk = 0
                    for j in range(4):
                        gy = ny + dy[j]
                        gx = nx + dx[j]
                        if 0 <= gy < N and 0 <= gx < M:
                            if matrix[gy][gx] == 'g':
                                chk = 1
                                break
                    if chk:
                        heappush(q, (c+1, ny, nx))
                    else:
                        heappush(q, (c, ny, nx))
                    visit[ny][nx] = 1

N, M = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
sty, stx = start()
BFS(sty, stx)