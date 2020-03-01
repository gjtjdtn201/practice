import sys
sys.stdin = open('좌표 정렬하기.txt', 'r')

c = []
for i in range(int(input())):c.append(tuple(map(int, input().split())))
for i in sorted(c, key=lambda x: (x[0], x[1])):print(*i)