import sys
sys.stdin = open('n과m 1.txt')

def p(k):
    if k == M:
        print(*a)
        return
    for i in range(N):
        if visit[i]:
            continue
        a[k] = arr[i]
        visit[i] = 1
        p(k+1)
        visit[i] = 0


N, M = map(int, input().split())

arr = list(range(1, N+1))
a = [0]*M
visit = [0]*(N+1)

p(0)