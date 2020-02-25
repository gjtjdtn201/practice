import sys
sys.stdin = open('톱니바퀴.txt', 'r')

from collections import deque

top = []
for i in range(4):
    top.append(deque(map(int, input())))
# 돌려야 할 기어
gear2 = [[0, 1, 2], [0, 1, 2], [2, 1, 0], [2, 1, 0]]
# 돌려질 바퀴번호
gear3 = [[1, 2, 3], [0, 2, 3], [3, 1, 0], [2, 1, 0]]
# 방향 리스트
chkl = [[0, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 1]]
# 돌릴 횟수
cnt = [[1, 1, 1], [0, 1, 1], [0, 1, 1], [1, 1, 1]]

K = int(input())

for i in range(K):
    num, chk = map(int, input().split())
    gear = []
    for j in range(3):
        gear.append([top[j][2], top[j+1][6]])
    stack = deque()
    stack.append((num-1, chk))
    if chk == 1:
        chk = -1
    else:
        chk = 1
    for x in range(3):
        if gear[gear2[num-1][x]][0] != gear[gear2[num-1][x]][1]:
            if chkl[num-1][x] == 1:
                if chk == 1:
                    chk = -1
                else:
                    chk = 1
            stack.append((gear3[num-1][x], chk))
        elif cnt[num-1][x] == 1:
            break

    while stack:
        gnum, chk2 = stack.popleft()
        if chk2 == 1:
            a = top[gnum].pop()
            top[gnum].appendleft(a)
        else:
            a = top[gnum].popleft()
            top[gnum].append(a)

ans = 0
for i in range(4):
    ans += top[i][0] * (2**i)

print(ans)