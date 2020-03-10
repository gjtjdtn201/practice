import sys
sys.stdin = open('최솟값으로 이동하기.txt', 'r')

for tc in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    a = []
    for i in range(N):
        x, y = map(int, input().split())
        a.append((x, y))
    ans = 0
    px, py = a[0][0], a[0][1]
    for z in range(1, N):
        x, y = a[z]
        if x > px and y > py:
            ans += min((x - px), (y - py)) + abs((x - px) - (y - py))
        elif x > px and y < py:
            ans += (x - px + py - y)
        elif x < px and y > py:
            ans += (px - x + y - py)
        elif x < px and y < py:
            ans += min((px - x), (py - y)) + abs((px - x) - (py - y))
        else:
            ans += abs(x - px) + abs(y - py)
        px, py = x, y
    print('#{} {}'.format(tc, ans))