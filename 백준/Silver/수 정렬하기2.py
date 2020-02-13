import sys
sys.stdin = open('수 정렬하기2.txt', 'r')

T = int(input())
a = []
for i in range(T):
    a.append(int(input()))
a.sort()
for i in a:
    print(i)