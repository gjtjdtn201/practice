import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    a = []
    ans = [0]+[1]*K+[0]
    ans2 = [1]*K + [0]
    ans3 = [0] + [1]*K
    cnt = 0
    for i in range(N):
        a.append(list(map(int, input().split())))
    for j in a:
        for i in range(N-K):
            if i == 0 and ans2 == j[0:len(ans2)]:
                cnt += 1
            elif i == (N-K-1) and ans3 == j[-len(ans3):]:
                cnt += 1
            elif ans == j[i:i+len(ans)]:
                cnt += 1
    a = list(zip(*a))
    ans = tuple(ans)
    ans2 = tuple(ans2)
    ans3 = tuple(ans3)

    for j in a:
        for i in range(N-K):
            if i == 0 and ans2 == j[0:len(ans2)]:
                cnt += 1
            elif i == (N-K-1) and ans3 == j[-len(ans3):]:
                cnt += 1
            elif ans == j[i:i+len(ans)]:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))