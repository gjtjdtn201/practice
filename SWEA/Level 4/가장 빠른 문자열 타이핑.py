import sys
sys.stdin = open('가장 빠른 문자열 타이핑.txt', 'r')

for tc in range(1, int(input())+1):
    A, B = list(input().split())
    i = ans = 0
    while i < len(A):
        if i+len(B) <= len(A):
            if A[i:i+len(B)] == B:
                ans += 1
                i += len(B)
                continue
        i += 1
        ans += 1
    print('#{} {}'.format(tc, ans))
