import sys
sys.stdin = open('늘어지는 소리 만들기.txt', 'r')

for tc in range(1, int(input())+1):
    a = list(input())
    H = int(input())
    b = list(map(int, input().split()))
    d = [0] * (len(a)+1)
    for i in b:
        d[i] += 1
    ans = ''
    for j in range(len(a)):
        ans += '-'*d[j] + a[j]
    print('#{} {}'.format(tc, ans+'-'*d[-1]))