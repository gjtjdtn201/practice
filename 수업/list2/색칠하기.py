import sys
sys.stdin = open("색칠하기.txt", "r")

T = int(input())

for i in range(1, T+1):
    matrix = [[0 for col in range(10)] for row in range(10)]
    N = int(input())
    for num in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for col in range(r1, r2+1):
            for row in range(c1, c2+1):
                if matrix[col][row] == color:
                    continue
                else:
                    matrix[col][row] += color
    cnt = 0
    for j in matrix:
        cnt += j.count(3)

    print(f'#{i} {cnt}')