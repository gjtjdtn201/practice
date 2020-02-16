import sys
sys.stdin = open('회전.txt', 'r')

from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    a = deque(map(int, input().split()))
    for i in range(M):
        n = a.popleft()
        a.append(n)
    print('#{} {}'.format(test_case, a[0]))