import sys
sys.stdin = open('올림픽 종목 투표.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ol = {}
    for i in B:
        for j in range(len(A)):
            if i >= A[j]:
                if j not in ol:
                    ol[j] = 1
                else:
                    ol[j] += 1
                break
    ans = cnt = 0
    j = 1
    for i, k in ol.items():
        if k > cnt:
            cnt = k
            ans = i+1
    print('#{} {}'.format(tc, ans))