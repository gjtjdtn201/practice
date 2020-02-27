import sys
sys.stdin = open('ACM 호텔.txt', 'r')

T = int(input())

for test_case in range(T):
    H, W, N = map(int, input().split())
    cnt = 1
    while True:
        if N <= H:
            floor = N
            break
        cnt += 1
        N -= H
    print(floor*100+cnt)