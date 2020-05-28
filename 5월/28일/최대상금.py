import sys
sys.stdin = open('최대상금.txt')

def DFS(pos, cnt):
    global ans
    tmp = int(''.join(number))
    if mydict.get((tmp, cnt)):
        return
    mydict[(tmp, cnt)] = 1
    if cnt == b:
        ans = max(ans, tmp)
        return
    for i in range(pos, N):
        for j in range(i+1, N):
            number[i], number[j] = number[j], number[i]
            DFS(i, cnt+1)
            number[j], number[i] = number[i], number[j]

for tc in range(1, int(input())+1):
    a, b = input().split()
    number = list(a)
    b = int(b)
    N = len(number)
    mydict = {}
    ans = 0
    DFS(0, 0)
    print('#{} {}'.format(tc, ans))