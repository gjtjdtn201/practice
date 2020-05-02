def storm():
    i, j = 5000, 5000
    delta = 1
    num = 1
    matrix[i][j] = num
    k = 0
    while True:
        k += 1
        for x in range(k):
            matrix[i][j] = num
            num += 1
            j += delta
            if j == 10001:
                return
        for y in range(k):
            matrix[i][j] = num
            num += 1
            i -= delta
        delta = -delta

# r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = -5000, -5000, -4998, -4998
r1 += 5000
c1 += 5000
r2 += 5000
c2 += 5000
matrix = [[0] * 10001 for _ in range(10001)]
storm()

digit = max(len(str(matrix[r1][c1])), len(str(matrix[r2][c2])),len(str(matrix[r1][c2])), len(str(matrix[r2][c1])))

for y in range(r1,r2+1):
    for x in range(c1,c2+1):
        ans = ' '*(digit - len(str(matrix[y][x]))) + str(matrix[y][x])
        print(ans, end=' ')
    print()