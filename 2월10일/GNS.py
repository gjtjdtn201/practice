import sys
sys.stdin = open('GNS.txt', 'r')

T = int(input())

a = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']

for test_case in range(1, T+1):
    A, B = input().split()
    word = list(input().split())
    ans = []
    for i in a:
        for j in word:
            if i == j:
                ans.append(j)
    ans = tuple(ans)
    print('#{}'.format(test_case))
    print(*ans)
