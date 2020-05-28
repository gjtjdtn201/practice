import sys
sys.stdin = open('n과m 1.txt')

def p(k, s, N, M):
    if k == M:
        print(*a)
    else:
        for i in range(s, N):
            a[k] = i+1
            p(k+1, i+1, N, M)

N, M = map(int, input().split())

a = [0]*M

p(0, 0, N, M)