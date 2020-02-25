import sys
sys.stdin = open('성공적인 공연 기획.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    people = list(map(int, input()))
    cnt = ans = 0
    for i in range(len(people)):
        if i > cnt and people[i]:
            ans += (i - cnt)
            cnt += (i - cnt)
        cnt += people[i]
    print('#{} {}'.format(test_case, ans))