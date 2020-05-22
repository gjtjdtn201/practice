import sys
sys.stdin = open('연산.txt')

from collections import deque

def BFS():
    while q:
        n = q.popleft()
        for i in [n+1, n-1, n*2, n-10]:
            if 0 <= i < PG and A[i] == -1:
                if i == M:
                    return A[n] + 1
                A[i] = A[n] + 1
                q.append(i)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    PG = 1000001
    A = [-1]*PG
    A[N] = 0
    q = deque()
    q.append(N)
    ans = BFS()
    print('#{} {}'.format(tc, ans))


