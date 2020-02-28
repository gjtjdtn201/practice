import sys
sys.stdin = open('보물상자 비밀번호.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    n = N // 4
    a = set()
    for z in range(n):
        num2 = num[z:] + num[:z]
        for i in range(0, N, n):
            a.add(int(num2[i:n+i], 16))
    print('#{} {}'.format(test_case, list(sorted(a, reverse=True))[K - 1]))