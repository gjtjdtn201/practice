import sys
sys.stdin = open('시험 감독.txt', 'r')

N = int(input())

A = list(map(int, input().split()))

B, C = map(int, input().split())

gd = 0
for i in A:
    a = i - B
    gd += 1
    if a <= 0:
        continue
    else:
        if a % C:
            gd += 1
        gd += a//C

print(gd)