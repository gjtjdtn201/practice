import sys
sys.stdin = open("안전 기지.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N, B = map(int,input().split())

    my_map = [[0 for x in range(N)] for y in range(N)]

    dx = [1,2,-1,-2,0,0,0,0]
    dy = [0,0,0,0,1,2,-1,-2]
    for i in range(B):
        y, x = map(int, input().split())
        for j in range(8):
            new_x = new_y = 0
            new_x = x-1 + dx[j]
            new_y = y-1 + dy[j]
            if N > new_x >= 0 and N > new_y >= 0:
                my_map[new_y][new_x] += 1
    ans = 0
    for x in range(N):
        for y in range(N):
           if my_map[y][x] > ans:
               ans = my_map[y][x]
    print('#{} {}'.format(test_case, ans))
