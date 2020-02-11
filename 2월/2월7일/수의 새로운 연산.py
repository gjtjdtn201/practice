import sys
sys.stdin = open('연습.txt', 'r')

def TS(val):
    i = 1
    ans = 0
    cnt = 0
    while ans < val:
        ans += i
        i += 1
        cnt += 1
    x = cnt - (ans - val)
    y = 1 + (ans - val)
    return x, y

def TS2(x,y):
    ans = 0
    for i in range(1, x + 1):
        ans += i
    for i in range(y - 1):
        ans += (x + i)
    return ans

T = int(input())

for test_case in range(1, T+1):
    p, q = map(int, input().split())
    x = TS(p)[0] + TS(q)[0]
    y = TS(p)[1] + TS(q)[1]

    print('#{} {}'.format(test_case, TS2(x, y)))