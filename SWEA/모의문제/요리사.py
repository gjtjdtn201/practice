import sys
sys.stdin = open('요리사.txt', 'r')

from itertools import combinations

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999
    for i in combinations(range(1,N+1), N//2):
        cnt = cnt2 = 0
        b = list(range(1, N+1))
        for j in i:
            b.remove(j)
            for k in i:
                cnt += matrix[j-1][k-1]
        for z in b:
            for y in b:
                cnt2 += matrix[z-1][y-1]
        cnt3 = abs(cnt - cnt2)
        ans = min(cnt3, ans)
    print('#{} {}'.format(tc, ans))