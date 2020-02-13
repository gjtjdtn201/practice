import sys
sys.stdin = open('스도쿠 검증.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    matrix = []
    ans = 1
    for i in range(9):
        matrix.append(list(map(int, input().split())))

    for i in matrix:
        if len(set(i)) != 9:
            ans = 0
            break
    chk = 0
    if ans == 1:
        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                nemo = []
                for m in range(3):
                    nemo.extend(matrix[m+l][k:k+3])
                if len(set(nemo)) != 9:
                    ans = 0
                    chk = 1
                    break
            if chk == 1:
                break

    if ans == 1:
        matrix = list(zip(*matrix))
        for j in matrix:
            if len(set(j)) != 9:
                ans = 0
                break

    print('#{} {}'.format(test_case, ans))