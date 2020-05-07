import sys
sys.stdin = open('화물 도크.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    time = [list(map(int, input().split())) for i in range(N)]
    time.sort(key= lambda x: x[1])
    end = time[0][1]
    cnt = 1
    for i in range(1, N):
        if time[i][0] >= end:
            end = time[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))