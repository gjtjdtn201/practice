import sys
sys.stdin = open('행렬 제곱.txt', 'r')

def MM(a, b):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000
    return result

N, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

B = bin(B)[2:]

unit = [[1 if x == y else 0 for x in range(N)] for y in range(N)]
tmp = unit[:]
for i in B:
    tmp = MM(tmp, tmp)
    if i == '1':
        tmp = MM(tmp, matrix)

for i in tmp:
    print(*i)