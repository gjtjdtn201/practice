import sys
sys.stdin = open('맥주 마시면서 걸어가기.txt', 'r')

from collections import deque

for tc in range(int(input())):
    n = int(input())
    sty, stx = map(int, input().split())
    shop = []
    for i in range(n):
        a, b = map(int, input().split())
        shop.append((a, b))
    edy, edx = map(int, input().split())
    shop.append((edy, edx))

    q = deque()
    visit = [(sty, stx)]
    q.append((sty, stx))
    while q:
        a, b = q.popleft()
        if (a, b) == (edy, edx):
            print('happy')
            break
        for ny, nx in shop:
            if (ny, nx) not in visit:
                dis = abs(ny-a) + abs(nx-b)
                if dis <= 1000:
                    q.append((ny, nx))
                    visit.append((ny, nx))
    else:
        print('sad')