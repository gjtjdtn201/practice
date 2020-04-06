import sys
sys.stdin = open('모래성 쌓기.txt', 'r')

from collections import deque

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    ans = -1
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    chk = 1
    q, qtmp = deque(), deque()
    for y in range(H):
        for x in range(W):
            # 파도를 기록
            if matrix[y][x] == '.':
                q.append((y, x))
            else:
                # 파도가 없으면 계산을 위해 입력을 숫자로 기록
                matrix[y][x] = int(matrix[y][x])
    # 파도가 없다? 끝
    if q:
        # 아쉽지만 있구요
        while chk:
            chk = 0
            while q:
                a, b = q.popleft()
                for i in range(8):
                    ny = a + dy[i]
                    nx = b + dx[i]
                    # 맵 벗어나면 거르고 성이 9면 무적이니까 거르고 파도 거르고
                    if 0 <= ny < H and 0 <= nx < W and matrix[ny][nx] != '.' and matrix[ny][nx] != 9:
                        # 큐가 파도의 좌표를 뽑았으니 근처에 있는 모래성을 -1 해줌
                        matrix[ny][nx] -= 1
                        # 파도에 못이겨서 성높이가 0 이되면 또다른 파도가 됨
                        if matrix[ny][nx] == 0:
                            # 제2의 물결 기록
                            qtmp.append((ny, nx))
                            # 넌 파도야
                            matrix[ny][nx] = '.'
                            # 파도가 새로 생겼으니까 q 반복을 위해 chk True 설정
                            chk = 1
            # 대충 1회차 추가 하라는 뜻
            ans += 1
            # 제 2의 물결을 파도로 배치
            q = deque(qtmp)
            # 제 3의 물결 기록용 deque 생성
            qtmp = deque()
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))