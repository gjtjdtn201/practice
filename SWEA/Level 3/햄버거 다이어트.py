import sys
sys.stdin = open('햄버거 다이어트.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    N, L = map(int, input().split())
    val = []
    cal = []
    for i in range(N):
        a, b = map(int, input().split())
        val.append(a)
        cal.append(b)
    c = []
    ans = 0
    for i in range(1 << N):
        cnt = cnt1 = 0
        for j in range(N):
            if i & (1 << j):
                cnt += val[j]
                cnt1 += cal[j]
        if cnt1 <= L:
            if ans < cnt:
                ans = cnt

    print('#{} {}'.format(test_case, ans))

