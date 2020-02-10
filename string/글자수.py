import sys
sys.stdin = open("글자수.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    ans = 0
    for i in str1:
        if ans < str2.count(i):
            ans = str2.count(i)

    print('#{} {}'.format(test_case, ans))