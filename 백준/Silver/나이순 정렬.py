import sys
sys.stdin = open('나이순 정렬.txt', 'r')

N = int(input())
c = []
for i in range(N):
    a, b = list(input().split())
    c.append((i, int(a), b))
for i in sorted(c, key=lambda x: (x[1], x[0])):
    print('{} {}'.format(i[1], i[2]))