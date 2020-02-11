import sys
sys.stdin = open('추억의 2048게임.txt','r')

def safe(y, x):
    return N > y >= 0 and N > x >= 0

def CG(result):
    for y in range(N):
        for x in range(N - 1):
            dx = 1
            for z in range(N):
                new_x = x + dx
                if safe(y, new_x):
                    if result[y][new_x] == 0:
                        dx += 1
                        continue
                    elif result[y][new_x] == result[y][x]:
                        result[y][x] *= 2
                        result[y][new_x] = 0
                    break

                else:
                    break
        else:
            cnt = 0
            for i3 in range(N):
                if result[y][i3] != 0:
                    result[y][cnt] = result[y][i3]
                    cnt += 1
            for i4 in range(cnt, N):
                result[y][i4] = 0


T = int(input())

for test_case in range(1, T + 1):
    N, chk = input().split()
    N = int(N)
    game = []
    for _ in range(N):
        game.append(list(map(int, input().split())))

    direction = {'left': 0, 'down': 1, 'right': 2, 'up': 3}
    r = direction[chk]

    for _ in range(r):
        game = list(zip(*game[::-1]))
    result = []
    for i in range(N):
        result.append(list(game[i]))
    CG(result)
    for _ in range(4 - r):
        result = list(zip(*result[::-1]))
    print('#{}'.format(test_case))
    for i in result:
        print(*i)