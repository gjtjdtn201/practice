import sys
sys.stdin = open('123.txt')

from collections import deque

N, M = map(int, input().split())
a = list(map(int, input().split()))
q = deque()
q.extend(range(1, N+1))
cnt = 0
for i in a:
    for j in range(len(q)):
        if q[j] == i:
            break
    if j > len(q)-j:
        chk = 1
        n = len(q)-j
    else:
        chk = 0
        n = j
    cnt += n
    q.rotate(n) if chk else q.rotate(-n)
    q.popleft()
print(cnt)