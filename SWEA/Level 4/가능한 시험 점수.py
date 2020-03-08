import sys
sys.stdin = open('가능한 시험 점수.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    point = list(map(int, input().split()))
    ss = sum(point)
    dp = [False for _ in range(ss+1)]
    dp[0] = True
    s = [0]
    for i in point:
        for j in range(len(s)):
            if not dp[i+s[j]]:
                s.append(i+s[j])
                dp[i+s[j]] = True
    print('#{} {}'.format(tc, len(s)))