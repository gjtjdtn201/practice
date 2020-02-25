import sys
sys.stdin = open('N-Queen.txt', 'r')

def solve(i):
    global ans
    if i == N:
        ans += 1
        return
    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):
            a[j] = b[i+j] = c[i-j+N-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+N-1] = False

N = int(input())

a = [False]*N
b = [False]*(2*N-1)
c = [False]*(2*N-1)

ans = 0
solve(0)

print(ans)