import sys
sys.stdin = open('수영장.txt', 'r')

def f(n, s):
    global ans
    if n >= 12:
        if ans > s:
            ans = s
    else:
        f(n+1, s+ticket[0]*plan[n])
        f(n+1, s+ticket[1])
        f(n+3, s+ticket[2])


T = int(input())

for test_case in range(1, T+1):
    ticket = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    ans = ticket[3]
    f(0, 0)
    print('#{} {}'.format(test_case, ans))