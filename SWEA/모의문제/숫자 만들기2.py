import sys
sys.stdin = open('숫자 만들기.txt', 'r')

def DFS(n, v, plus, minus, multi, divis):
    global maxa, mina
    if n == N:
        maxa = max(maxa, v)
        mina = min(mina, v)
        return
    if plus > 0: DFS(n+1, int(v + num[n]), plus - 1, minus, multi, divis)
    if minus > 0: DFS(n+1, int(v - num[n]), plus, minus - 1, multi, divis)
    if multi > 0: DFS(n+1, int(v * num[n]), plus, minus, multi - 1, divis)
    if divis > 0: DFS(n+1, int(v / num[n]), plus, minus, multi, divis - 1)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    maxa, mina = -10**6, 10**6
    DFS(1, num[0], oper[0], oper[1], oper[2], oper[3])

    print('#{} {}'.format(test_case, maxa - mina))