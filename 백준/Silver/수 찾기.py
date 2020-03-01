import sys
sys.stdin = open('수 찾기.txt', 'r')

N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        print(1)
    else:
        print(0)