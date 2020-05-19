import sys
sys.stdin = open('역사.txt')

n, k = map(int, input().split())
matrix = [[0]*n for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] + matrix[k][j] == 2:
                matrix[i][j] = 1

for i in range(int(input())):
    a, b = map(int, input().split())
    if matrix[a-1][b-1] + matrix[b-1][a-1] == 0:
        print(0)
    elif matrix[a-1][b-1] > matrix[b-1][a-1]:
        print(-1)
    else:
        print(1)