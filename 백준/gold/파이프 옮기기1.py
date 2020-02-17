import sys
sys.stdin = open('파이프 옮기기1.txt', 'r')

from collections import deque

N = int(input())

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))
# 0은 아래로 1은 오른쪽 2는 대각선
dy = [-1, 0, -1]
dx = [0, 1, 1]
# 0은 가로일때 1은 세로일때 2는 대각선일때
direction = [[1, 2], [0, 2], [0, 1, 2]]

queue = deque()
queue.append(0, 1)
chk = 0
while queue:
    a, b = queue.popleft()
    for z in direction[chk]:
        ny = a + dy[z]
        nx = b + dx[z]


for i in matrix:
    print(i)