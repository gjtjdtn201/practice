import sys
sys.stdin = open("test.txt", "r")


def DQ(a):
    if len(a) <= 1:
        return
    mid = len(a) // 2
    g1 = a[mid:]
    g2 = a[:mid]
    DQ(g1)
    DQ(g2)

    if g1[0] == '1' and g2[0] == '2':
        g1[0] = 0
        return g2
    elif g1[0] == '2' and g2[0] == '3':
        g1[0] = 0
        return g2
    elif g1[0] == '3' and g2[0] == '1':
        g1[0] = 0
        return g2
    else:
        g2[0] = 0
        return g1




# 1 가위 2 바위 3 보
# 1 2 2승리 2 3 3승리 1 3 1승리


T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    ml = list(input().split())
    a = []
    ans = DQ(ml)
    print('#{} {}'.format(test_case, ans))