import sys
sys.stdin = open('크로스워드 만들기.txt', 'r')

M, N = input().split()
matrix = [['.'for _ in range(len(M))] for __ in range(len(N))]
chk = 0
for y in range(len(M)):
    for x in range(len(N)):
        if M[y] == N[x]:
            chk = 1
            break
    if chk == 1:
        break

for i in range(len(M)):
    matrix[x][i] = M[i]
for i in range(len(N)):
    matrix[i][y] = N[i]

for i in matrix:
    print(''.join(i))