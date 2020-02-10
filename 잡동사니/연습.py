import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1, T + 1):
    N, chk = input().split()
    n = int(N)
    game = []
    for _ in range(n):
        game.append(list(map(int, input().split())))

    direction = {'left': 0, 'down': 1, 'right': 2, 'up': 3}
    r = direction[chk]

    for _ in range(r):
        game = list(zip(*game[::-1]))

    result = [[] for _ in range(n)]
    for i in range(n):
        line = list(x for x in game[i])
        check = 0
        jn = 1
        for j in range(n):
            if jn != 1:
                jn -= 1
                continue
            cur = line[j]
            if j + jn >= n:
                result[i].append(cur)
                break
            nex = line[j + jn]
            if cur == 0:
                continue
            if nex == 0:
                while nex == 0:
                    jn += 1
                    if j + jn >= n:
                        result[i].append(cur)
                        break
                    nex = line[j + jn]
            if j + jn >= n:
                break

            if cur == nex:
                result[i].append(cur * 2)
                line[j + jn] = 0
            else:
                result[i].append(cur)

    for res in result:
        temp = len(res)
        if temp != n:
            for _ in range(n - temp):
                res.append(0)

    for _ in range(4 - r):
        result = list(zip(*result[::-1]))

    print('#{}'.format(test_case))
    for re in result:
        print(*re)