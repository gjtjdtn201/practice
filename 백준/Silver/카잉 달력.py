import sys
sys.stdin = open('카잉 달력.txt', 'r')

for tc in range(int(input())):
    M, N, x, y = map(int, input().split())
    while x <= N*M:
        if (x-y)%N == 0:
            print(x)
            break
        x += M
    else:
        print(-1)