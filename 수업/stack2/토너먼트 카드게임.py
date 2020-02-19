import sys
sys.stdin = open("토너먼트 카드게임.txt", "r")

def excute(g1,g2):
    if ml[g1-1] == '1' and ml[g2-1] == '2':
        return g2
    elif ml[g1-1] == '2' and ml[g2-1] == '3':
        return g2
    elif ml[g1-1] == '3' and ml[g2-1] == '1':
        return g2
    else:
        return g1


def DQ(st, ed):
    if st == ed:
        return st
    mid = (st+ed) // 2
    g1 = DQ(st, mid)
    g2 = DQ(mid+1, ed)
    return excute(g1, g2)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ml = list(input().split())
    ans = DQ(1, N)
    print('#{} {}'.format(test_case, ans))