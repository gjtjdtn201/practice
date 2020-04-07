import sys
sys.stdin = open('0과1.txt', 'r')

def DFS(a):
    global ans
    if int(a) % n == 0:
        ans = int(a)
        return
    else:
        if len(a) < 100 and ans == 0:
            DFS(a+'1')
            DFS(a+'0')

for tc in range(int(input())):
    n = int(input())
    ans = 0
    DFS('1')
    if ans != 0:
        print(ans)
    else:
        print('BRAK')