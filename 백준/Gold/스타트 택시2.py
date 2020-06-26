import sys
sys.stdin = open('스타트 택시.txt')

from collections import deque

def find_customer(taxi_row, taxi_col):

    queue = deque()
    queue.append((taxi_row, taxi_col))
    chk = [[0] * N for _ in range(N)]
    chk[taxi_row][taxi_col] = 1
    min_dist = 987654321
    min_row, min_col, min_cust = 987654321, -1, -1
    while queue:

        row, col = queue.popleft()
        # 가장 짧은 손님을 구하면 가장 작은 열, 작은 행 체크하고 마지막에 리턴
        if maplist[row][col] > 1 and chk[row][col] <= min_dist:
            min_dist = chk[row][col]

            if min_row > row:
                min_row = row
                min_col = col
                min_cust = maplist[row][col]
            elif min_row == row and min_col > col:
                min_col = col
                min_cust = maplist[row][col]
            # print(row, col)
            # print(min_col, min_row)

        for idx in range(4):
            next_row = row + dy[idx]
            next_col = col + dx[idx]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if chk[next_row][next_col] or maplist[next_row][next_col] == 1:
                continue

            chk[next_row][next_col] = chk[row][col] + 1
            queue.append((next_row, next_col))


    # 손님 발견시 해당 위치 맵 0 으로 변경
    if min_col >= 0:
        maplist[min_row][min_col] = 0
    # 발견못했을때 mis_dist가 987654321 이여서 cur_fuel에서 뺐을때 음수가 됨
    return min_row, min_col, min_cust, min_dist-1



def find_dest(row, col, cust_num):
    queue = deque()
    queue.append((row, col))

    chk = [[0] * N for _ in range(N)]
    chk[row][col] = 1

    # 맵과 손님번호가 같으면 목적지를 찾은 것
    # 그 위치와 거리 리턴
    while queue:
        row, col = queue.popleft()

        if maplist_dest[row][col] == cust_num:
            maplist_dest[row][col] = 0

            return row, col, chk[row][col]-1

        for idx in range(4):
            next_row = row + dy[idx]
            next_col = col + dx[idx]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if chk[next_row][next_col] or maplist_dest[next_row][next_col] == 1:
                continue

            chk[next_row][next_col] = chk[row][col] + 1
            queue.append((next_row, next_col))

    return -1, -1, 987654321

N, M, cur_fuel = map(int, input().split())

maplist = [list(map(int, input().split())) for _ in range(N)]
maplist_dest = [[0] * N for _ in range(N)]

for i in range(N):
    maplist_dest[i] = list(maplist[i])

taxi_row, taxi_col = map(int, input().split())
taxi_row -= 1
taxi_col -= 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


for i in range(2, M+2):
    sty, stx, edy, edx = map(int, input().split())
    maplist[sty-1][stx-1] = i
    maplist_dest[edy-1][edx-1] = i

# for i in range(N):
#     print(maplist[i])
# print()
# for i in range(N):
#     print(maplist_dest[i])
# print()
for _ in range(M):
    # 택시의 현재위치에 손님이 있을 경우
    if maplist[taxi_row][taxi_col] > 1:
        customer_num = maplist[taxi_row][taxi_col]
        maplist[taxi_row][taxi_col] = 0
        dist = 0
    # 그렇지 않을경우 find_customer를 통해 값 구함
    else:
        taxi_row, taxi_col, customer_num, dist = find_customer(taxi_row, taxi_col)
        cur_fuel -= dist
        if cur_fuel <= 0:
            cur_fuel = -1
            break
    # print('dist', dist)
    # print(cur_fuel)
    # find_dest 를 통해 해당 손님의 목적지 까지의 거리를 구한다.
    taxi_row, taxi_col, dist = find_dest(taxi_row, taxi_col, customer_num)

    cur_fuel -= dist
    if cur_fuel < 0:
        cur_fuel = -1
        break
    else:
        cur_fuel += dist * 2
    # print('dist_dest', dist)
    # print(cur_fuel)
    # print()

print(cur_fuel)