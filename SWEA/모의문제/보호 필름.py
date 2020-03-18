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
            if cnt0 >= K:
                break
            elif K - cnt0 > D - 1 - y:
                return False
        else:
            return False
    return True

def IJ(n, k, idx):
    global ans
    if n <= k and n < ans:
        if chk(matrix):
            ans = n
            return
    elif K-n > D-1 - idx:
        return
    if n < k:
        for i in range(idx, D):
            if not visit[i]:
                a = matrix[i]
                visit[i] = True
                matrix[i] = [0]*W
                IJ(n + 1, k, i + 1)
                matrix[i] = [1]*W
                IJ(n + 1, k, i + 1)
                matrix[i] = a
                visit[i] = False
    return

for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    visit = [False] * D
    ans = K
    if K == 1:
        ans = 0
    elif chk(matrix):
        ans = 0
    else:
        IJ(0, K-1, 0)

    print('#{} {}'.format(tc, ans))