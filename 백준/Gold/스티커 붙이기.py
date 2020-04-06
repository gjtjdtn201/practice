import sys
sys.stdin = open('스티커 붙이기.txt', 'r')

def bond(y, x):
    for r in range(R):
        for c in range(C):
            if matrix[y + r][x + c] and ST[r][c]:
                return False
    return True

N, M, K = map(int, input().split())
matrix = [[0]*M for _ in range(N)]
ans = 0
for i in range(K):
    R, C = map(int, input().split())
    ST = [list(map(int, input().split())) for _ in range(R)]
    cnt = 4
    chk = 0
    while cnt:
        cnt -= 1
        for y in range(N-R+1):
            if chk:
                break
            for x in range(M-C+1):
                if chk:
                    break
                elif bond(y, x):
                    chk = 1
                    for r in range(R):
                        for c in range(C):
                            if ST[r][c] == 1:
                                matrix[y + r][x + c] = 1
                                ans += 1
        if chk:
            break
        ST = list(zip(*ST[::-1]))
        R, C = C, R
print(ans)