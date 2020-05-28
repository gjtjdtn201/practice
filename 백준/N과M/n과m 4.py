import sys
sys.stdin = open('n과m 1.txt')

def p(n, s):
    if n == M:
        print(*a)
        return
    for i in range(1, N+1):
        if i < s:
            continue
        a[n] = i
        p(n+1, i)

N, M = map(int, input().split())
a = [0]*M
p(0, 1)