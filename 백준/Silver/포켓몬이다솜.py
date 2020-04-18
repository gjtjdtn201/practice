import sys
sys.stdin = open('포켓몬이다솜.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = dict()
b = []
for i in range(N):
    c = input().rstrip()
    a[c] = i
    b.append(c)
for j in range(M):
    d = input().rstrip()
    if d.isdecimal():
        print(b[int(d)-1])
    else:
        print(a[d]+1)