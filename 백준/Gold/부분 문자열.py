import sys
sys.stdin = open('부분 문자열.txt', 'r')

import sys
# input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()
N = len(S)
M = len(P)
i = 0
ans = 0
while i <= N-M:
    j = M -1
    while j >= 0:
        if P[j] != S[i+j]:
            for k in range(M-2,-1,-1):
                if P[k] == S[k+M-1]:
                    move = M-k-1
                    break
            else:
                move = M
            break
        j -= 1
    if j == -1:
        ans = 1
        break
    else:
        i += move
print(ans)