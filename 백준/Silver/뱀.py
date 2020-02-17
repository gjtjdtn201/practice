import sys
sys.stdin = open('뱀.txt', 'r')

from collections import deque

N = int(input())

matrix = [[0 for _ in range(N)] for __ in range(N)]

K = int(input())
apple = []
for i in range(K):
    ay, ax = map(int, input().split())
    apple.append((ay-1, ax-1))

L = int(input())

X = []
C = deque()

for i in range(L):
    x, c = list(input().split())
    X.append(int(x))
    C.append(c)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

stack = [(0, 0)]
visit = deque()

z = 1
cnt = -1
k = 0
while stack:
    a, b = stack.pop()
    if (a, b) not in visit:
        visit.append((a, b))
    cnt += 1

    if cnt == X[k]:
        if k < L - 1:
            k += 1
        d = C.popleft()
        if d == 'L':
            z -= 1
            if z == -1:
                z = 3
        elif d == 'D':
            z += 1
            if z == 4:
                z = 0

    ny = a + dy[z]
    nx = b + dx[z]
    if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visit:
        stack.append((ny, nx))
        if (ny, nx) in apple:
            apple.remove((ny, nx))
            continue
        visit.popleft()


print(cnt+1)