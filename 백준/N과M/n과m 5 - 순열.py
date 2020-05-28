import sys
sys.stdin = open('n과m 5 - 순열.txt')

def p(n):
    if n == M:
        print(*a)
        return
    for i in range(N):
        if visit[i]:
            continue
        a[n] = arr[i]
        visit[i] = 1
        p(n+1)
        visit[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

a = [0]*M
visit = [0]*N
p(0)