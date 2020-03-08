import sys
sys.stdin = open('최적 경로.txt', 'r')

from itertools import permutations

for tc in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))
    com = (a[1], a[0])
    house = (a[3], a[2])
    cos = []
    for i in range(4, len(a)-1, 2):
        cos.append((a[i+1], a[i]))
    ans = float('inf')
    for i in permutations(cos):
        path = [com, *list(i), house]
        dis = 0
        for j in range(len(path)-1):
            dis += abs(path[j][0] - path[j+1][0]) + abs(path[j][1] - path[j+1][1])
        ans = min(ans, dis)
    print('#{} {}'.format(tc, ans))