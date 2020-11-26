import sys
sys.stdin = open('미아 노트.txt')

import sys
input = sys.stdin.readline

N, H, W = map(int, input().split())
ans = [0] * (N*W)
for i in range(H):
    A = list(input().rstrip())
    for j in range(N*W):
        if A[j] == '?':
            continue
        ans[j] = A[j]
res = ''
for i in range(0, N*W, W):
    for j in range(W):
        if ans[i+j]:
            res += ans[i+j]
            break
    else:
        res += '?'
print(res)