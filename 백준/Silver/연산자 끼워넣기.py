import sys
sys.stdin = open('연산자 끼워넣기.txt', 'r')

def DFS(n , v):
    global maxa, mina
    if n == N:
        maxa = max(maxa, v)
        mina = min(mina, v)
        return
    if oper[0] > 0:
        oper[0] -= 1
        DFS(n + 1, v + num[n])
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        DFS(n + 1, v - num[n])
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        DFS(n + 1, v * num[n])
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        if v < 0:
            DFS(n + 1, -(-v // num[n]))
        else:
            DFS(n + 1, v // num[n])
        oper[3] += 1

N = int(input())

num = list(map(int, input().split()))
oper = list(map(int, input().split()))
maxa, mina = -10**9, 10**9
DFS(1, num[0])
print(maxa)
print(mina)