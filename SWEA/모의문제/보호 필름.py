import sys
sys.stdin = open('보호 필름.txt', 'r')

def chk(c_matrix):
    for x in range(W):
        cnt0 = 1
        chk1 = matrix[0][x]
        for y in range(1, D):
            if c_matrix[y][x] == chk1:
                cnt0 += 1
            else:
                cnt0 = 1
            chk1 = c_matrix[y][x]
            if cnt0 == K:
                break
            elif K-cnt0 > D-1-y:
                return False
        else:
            return False
    return True

def IJ(n, k, idx):
    global res
    if res == 1:
        return
    if n == k:
        if chk(matrix):
            res = 1
        return
    elif K-n > D-1 - idx:
        return
    for i in range(idx, D):
        a = matrix[i][:]
        matrix[i] = [0]*W
        IJ(n + 1, k, idx + 1)
        matrix[i] = [1]*W
        IJ(n + 1, k, idx + 1)
        matrix[i] = a

for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    ans = 1
    res = 0
    if K == 1:
        ans = 0
    elif chk(matrix):
        ans = 0
    else:
        while ans < K:
            IJ(0, ans, 0)
            if res == 1:
                break
            ans += 1

    print('#{} {}'.format(tc, ans))