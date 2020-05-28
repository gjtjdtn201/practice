import sys
sys.stdin = open('n과m 5 - 순열.txt')

def p(n):
    if n == M:
        print(*a)
        return
    for i in range(N):
        a[n] = arr[i]
        p(n+1)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

a = [0]*M
p(0)