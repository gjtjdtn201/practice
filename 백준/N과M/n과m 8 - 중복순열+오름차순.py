import sys
sys.stdin = open('n과m 5 - 순열.txt')

def p(n, s):
    if n == M:
        print(*a)
        return
    for i in range(N):
        if arr[i] < s:
            continue
        a[n] = arr[i]
        p(n+1, arr[i])

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

a = [0]*M
p(0, 1)