import sys
sys.stdin = open('Ladder1.txt', 'r')

for test_case in range(10):
    T = int(input())
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))

    direction = [(-1, 0), (0, 1), (0, -1)]
    chk = 0

    for i in range(100):
        if matrix[99][i] == 2:
            x = i
            break
    y = 99
    while y > 0:
        y += direction[chk][0]
        x += direction[chk][1]

        if y < 100 and x + 1 < 100 and chk != 2 and matrix[y][x + 1] == 1:
                chk = 1
        elif y < 100 and x - 1 >= 0 and chk != 1 and matrix[y][x - 1] == 1:
                chk = 2
        else:
            chk = 0

    print('#{} {}'.format(T, x))