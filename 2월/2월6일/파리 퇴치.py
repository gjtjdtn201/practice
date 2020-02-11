import sys
sys.stdin = open('파리 퇴치.txt','r')

T = int(input())

for test_case in range(1,1+T):
    N, M = map(int, input().split())

    PT = []
    for i in range(N):
        PT.append(list(map(int, input().split())))
    ans = 0
    maxval = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            maxval =0
            for px in range(M):
                for py in range(M):
                    maxval += PT[x+px][y+py]
            if ans < maxval:
                ans = maxval

    print('#{} {}'.format(test_case, ans))