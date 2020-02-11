import sys
sys.stdin = open("이진탐색.txt", "r")

def bs(P, val):
    l = 1
    r = P
    c = int((l+r)/2)
    cnt = 1
    while val != c:
        if val < c:
            r = c
            c = int((l+r)/2)
            cnt += 1
        elif val > c:
            l = c
            c = int((r+l)/2)
            cnt += 1
        else:
            break
    return cnt

T = int(input())

for i in range(1, T+1):
    P, A, B = list(map(int, input().split()))
    ans = 0
    if bs(P, A) > bs(P, B):
        ans = 'B'
    elif bs(P, A) == bs(P, B):
        ans = 0
    else:
        ans = 'A'

    print(f'#{i} {ans}')