import sys
sys.stdin = open('n과m 9 - 순열+중복제거.txt')

def p(n, s):
    if n == M:
        res.add(tuple(a))
        return
    for i in range(N):
        if visit[i] or arr[i] < s:
            continue
        a[n] = arr[i]
        visit[i] = 1
        p(n+1, arr[i])
        visit[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

a = [0]*M
visit = [0]*N
res = set()
p(0, 1)
res = list(res)
res.sort()
for i in res:
    print(*i)