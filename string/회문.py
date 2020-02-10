import sys
sys.stdin = open("회문.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    M, N = list(map(int, input().split()))
    sl = []
    ans = 0
    for i in range(M):
        al = list(input())
        sl.append(al)
        for i in range(M-N+1):
            if al[i:N+i] == al[i:N+i][::-1]:
                ans = ''.join(al[i:N+i])
    if ans == 0:
        sl = list(zip(*sl))
        for j in sl:
            for k in range(M-N+1):
                if j[k:N+k] == j[k:N+k][::-1]:
                    ans = ''.join(j[k:N+k])

    print('#{} {}'.format(test_case, ans))