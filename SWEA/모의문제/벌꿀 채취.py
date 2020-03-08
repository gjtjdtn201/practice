import sys
sys.stdin = open('벌꿀 채취.txt', 'r')

def mmax(num, idx, tmp_sum, result) :
    if (tmp_sum > C) :
        return 0
    if (idx == M) :
        return result

    value = honey[num][idx] ** 2
    return max(mmax(num, idx + 1, tmp_sum + honey[num][idx], result + value), mmax(num, idx + 1, tmp_sum, result))


TC = int(input())

for test_case in range(1, TC + 1) :
    N, M, C = map(int, input().split())
    maplist = [list(map(int, input().split())) for _ in range(N)]
    chk = [[False for _ in range(N)] for _ in range(N)]
    honey = []
    total = 0
    cnt = 0

    for i in range(N) :
        for j in range(N - M + 1) :
            for k in range(M) :
                chk[i][j + k] = True
            honey.append(maplist[i][j :j + M])
            for y in range(N) :
                for x in range(N - M + 1) :
                    for a in range(M) :
                        if (chk[y][x + a] != False) :
                            break
                    else :
                        honey.append(maplist[y][x :x + M])
                        worker1 = mmax(0, 0, 0, 0)
                        worker2 = mmax(1, 0, 0, 0)
                        total = max(total, worker1 + worker2)
                        honey.pop()
            honey = []
            for k in range(M) :
                chk[i][j + k] = False

    print("#{} {}".format(test_case, total))