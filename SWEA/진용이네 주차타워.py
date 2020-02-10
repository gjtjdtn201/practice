import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    n, m = map(int, input().split())
    R = []
    W = []
    rest = [0]*n
    ans = 0
    tmp = []
    for i in range(n):
        R.append(int(input()))
    for i in range(m):
        W.append(int(input()))
    for i in range(m*2):
        a = int(input())
        if a > 0:
            tmp.append(a)
        else:
            rest[rest.index(abs(a))] = 0
        if 0 in rest and tmp:
            b = rest.index(0)
            car = tmp.pop(0)
            ans += R[b]*W[car-1]
            rest[b] = car

    print('#{} {}'.format(test_case, ans))