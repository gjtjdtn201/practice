import sys
sys.stdin = open('줄기세포배양.txt')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stem = []
    board = {}
    ans = 0

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for y in range(N):
        for x in range(M):
            if matrix[y][x] > 0:
                stem.append((matrix[y][x], y, x, 0))
                board[(y, x)] = matrix[y][x]
                ans += 1
    for i in range(K):
        stem.sort()
        new = []
        while stem:
            vit, y, x, cnt = stem.pop()
            if cnt == vit:
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if not board.get((ny, nx)):
                        board[(ny, nx)] = vit
                        new.append((vit, ny, nx, 0))
                        ans += 1
            cnt += 1
            if cnt == vit*2:
                ans -= 1
            else:
                new.append((vit, y, x, cnt))
        stem = new
    print('#{} {}'.format(tc, ans))