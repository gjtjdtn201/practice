import sys
sys.stdin = open('탐사.txt')

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
visit = [[987654321]*(K+1) for _ in range(K+1)]
chk = 1
for i in range(1, K+1):
    visit[i][i-1] = 0
    visit[i][i] = 0
    visit[i-1][i] = 1
for i in range(N):
    a, b, c = map(int, input().split())
    if visit[a-1][b] > c:
        visit[a-1][b] = c
    visit[b][a-1] = -c
for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            visit[j][k] = min(visit[j][k], visit[j][i]+visit[i][k])
for i in range(K+1):
    if visit[i][i] < 0:
        print('NONE')
        chk = 0
        break
if chk:
    for i in range(K):
        print('#' if visit[0][i+1]-visit[0][i] > 0 else '-',end='')