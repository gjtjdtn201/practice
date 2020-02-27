import sys
sys.stdin = open('행렬찾기.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    cnt = 0
    for y in range(n):
        for x in range(n):
            if matrix[y][x] != 0:
                cnt += 1
                for x1 in range(x, n):
                    if matrix[y][x1] == 0 or x1 == n-1:
                        break
                for y1 in range(y, n):
                    if matrix[y1][x] == 0 or y1 == n-1:
                        break
                ans.append(((y1-y)*(x1-x), y1-y, x1-x))
                for y2 in range(y, y1):
                    for x2 in range(x, x1):
                        matrix[y2][x2] = 0
    ans.sort(key=lambda x: (x[0], x[1]))
    res = ''
    for i in ans:
        res += str(i[1]) + ' ' + str(i[2]) + ' '
    print('#{} {} {}'.format(test_case, cnt, res.rstrip()))