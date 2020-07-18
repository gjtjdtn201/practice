import sys
sys.stdin = open('당구공을 넣자.txt')

M, N, x, y, mx, my = map(int, input().split())

stack = [(y, x)]
while stack:
    a, b = stack.pop()
    ny, nx = a, b
    while 0 <= ny < N and 0 <= nx < M:
        ny += my
        nx += mx
    print()