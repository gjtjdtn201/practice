import sys
sys.stdin = open('숫자 만들기.txt', 'r')

def DFS(n, v):
    global maxa, mina
    if n == N:
        maxa = max(maxa, v)
        mina = min(mina, v)
        return
    if oper[0] > 0:
        oper[0] -= 1
        DFS(n+1, int(v + num[n]))
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        DFS(n+1, int(v - num[n]))
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        DFS(n+1, int(v * num[n]))
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        DFS(n+1, int(v / num[n]))
        oper[3] += 1

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    maxa, mina = -10**6, 10**6
    DFS(1, num[0])

    print('#{} {}'.format(test_case, maxa - mina))