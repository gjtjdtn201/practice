import sys
sys.stdin = open('삼성시의 버스 노선.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ryu = [0]*5000
    for i in range(N):
        A,B = map(int, input().split())
        A -= 1
        B -= 1
        for j in range(A,B+1):
            ryu[j] += 1


    P = int(input())
    ans = ''
    for i in range(P):
        ans += str(ryu[int(input()) - 1]) + ' '

    print('#{} {}'.format(test_case, ans))