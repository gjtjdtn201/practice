import sys
sys.stdin = open('색종이.txt', 'r')

T = int(input())

matrix = [[0 for y in range(100)] for x in range(100)]

for i in range(T):
    a, b = map(int,input().split())
    for x in range(a,a+10):
        for y in range(b,b+10):
            matrix[x][y] = 1
cnt = 0
for i in matrix:
    cnt += i.count(1)

print(cnt)