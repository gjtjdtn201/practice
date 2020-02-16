import sys
sys.stdin = open('탈주범 검거.txt', 'r')

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    # N 맵 세로, M 맵 가로, R 맨홀 세로, C 맨홀 가로, L 경과시간
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().split())))

    dy = [1, -1, 0, 0] # 아래, 위, 오른쪽, 왼쪽
    dx = [0, 0, 1, -1]
    direction = [[]]
    direction.append([0, 1, 2, 3])
    direction.append([0, 1])
    direction.append([2, 3])
    direction.append([1, 2])
    direction.append([0, 2])
    direction.append([0, 3])
    direction.append([1, 3])
    # 1이면 0이 있어야 하고 0이면 1이 있어야 하고 2면 3이있어야 하고 3이면 2가 있어야함
    queue = deque()
    queue.append((R, C))
    visit = [[0 for _ in range(M)] for __ in range(N)]
    visit[R][C] = 1
    cnt = cnt2 = 1
    while cnt < L:
        k = 0
        while cnt2 > 0:
            a, b = queue.popleft()
            for i in direction[matrix[a][b]]:
                ny = a + dy[i]
                nx = b + dx[i]
                if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] != 0 and visit[ny][nx] == 0:
                    if (i == 0 and 1 in direction[matrix[ny][nx]]) or (i == 1 and 0 in direction[matrix[ny][nx]]) or(i == 2 and 3 in direction[matrix[ny][nx]]) or (i == 3 and 2 in direction[matrix[ny][nx]]):
                        queue.append((ny, nx))
                        visit[ny][nx] = 1
                        k += 1
            cnt2 -= 1
        cnt += 1
        cnt2 = k

    ans = 0
    for i in visit:
        ans += sum(i)
    print('#{} {}'.format(test_case, ans))