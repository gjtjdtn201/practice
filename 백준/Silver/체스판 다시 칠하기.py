import sys
sys.stdin = open('체스판 다시 칠하기.txt', 'r')

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
chk = ['B', 'W']
ans = N * M
for i in range(N-8+1):
    for j in range(M-8+1):
        c_matrix = []
        cnt = cnt2 = 0
        for k in range(8):
            c_matrix.append(matrix[i+k][j:8+j])
        for y in range(8):
            for x in range(8):
                if M % 2 == 1 and y % 2 == 1:
                    z = 1
                if c_matrix[y][x] != chk[(y+x) % 2]:
                    cnt += 1
                else:
                    cnt2 += 1
        ans = min(ans, min(cnt, cnt2))
print(ans)