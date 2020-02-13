import sys
sys.stdin = open('색종이2.txt', 'r')

T = int(input())

matrix = [[0 for y in range(100)] for x in range(100)]

for i in range(T):
    a, b = map(int,input().split())
    for x in range(a,a+10):
        for y in range(b,b+10):
            matrix[x][y] = 1
cnt = 0
for i in matrix:
    for j in range(99):
        if i[j] == 0 and i[j+1] == 1:
            cnt += 2
matrix = list(zip(*matrix))
for i in matrix:
    for j in range(99):
        if i[j] == 0 and i[j+1] == 1:
            cnt += 2

print(cnt)