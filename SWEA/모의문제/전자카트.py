import sys
sys.stdin = open('전자카트.txt', 'r')

from itertools import permutations

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    for i in permutations(range(1, N)):
        cnt = chk = 0
        for j in i:
            cnt += matrix[chk][j]
            if cnt > ans:
                break
            chk = j
        cnt += matrix[chk][0]
        ans = min(ans, cnt)
    print('#{} {}'.format(tc, ans))