import sys
sys.stdin = open('미로 탈출하기.txt')

import sys
input = sys.stdin.readline

def DFS(sty, stx):
    global cnt
    stack = [sty, stx]
    bt = [(sty, stx)]
    while stack:
        a, b = stack.pop()
        if 0 > sty or N <= sty or 0 > stx or M <= stx:
            visit[sty][stx]
            for by, bx in bt:
                visit[by][bx] = 1
                cnt += 1
            return



N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

move = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

visit = [[0]*M for _ in range(N)]

cnt = 0

for y in range(N):
    for x in range(M):
        if not visit[y][x]:
            if DFS(y, x):
                cnt += 1
        else:
            cnt += 1