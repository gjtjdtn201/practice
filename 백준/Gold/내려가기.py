import sys
sys.stdin = open('내려가기.txt', 'r')

import sys
input = sys.stdin.readline

tmax = [0, 0, 0]
tmin = [0, 0, 0]
a = [0, 0, 0]
b = [0, 0, 0]
for i in range(int(input())):
    c = list(map(int, input().split()))
    tmax[0] = max(a[0], a[1]) + c[0]
    tmax[1] = max(a[0], a[1], a[2]) + c[1]
    tmax[2] = max(a[1], a[2]) + c[2]
    tmin[0] = min(b[0], b[1]) + c[0]
    tmin[1] = min(b[0], b[1], b[2]) + c[1]
    tmin[2] = min(b[1], b[2]) + c[2]
    a = tmax[:]
    b = tmin[:]
print(max(tmax), min(tmin))