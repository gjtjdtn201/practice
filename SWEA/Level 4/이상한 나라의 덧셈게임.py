import sys
sys.stdin = open('이상한 나라의 덧셈게임','r')

T = int(input())

for test_case in range(1, T+1):
    N = input()
    if ((sum(map(int, N)) - 1) // 9 + len(N)) % 2:
        ans = 'B'
    else:
        ans = 'A'
    print('#{} {}'.format(test_case, ans))
