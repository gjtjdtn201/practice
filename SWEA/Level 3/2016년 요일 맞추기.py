import sys
sys.stdin = open('2016년 요일 맞추기.txt', 'r')

T = int(input())

a = dict()
a[1] = 31
a[2] = 29
a[3] = 31
a[4] = 30
a[5] = 31
a[6] = 30
a[7] = 31
a[8] = 31
a[9] = 30
a[10] = 31
a[11] = 30

for test_case in range(1, T+1):
    m, d = map(int, input().split())
    cnt = d + 3
    for i in range(1,m):
        cnt += a[i]

    print('#{} {}'.format(test_case, cnt%7))