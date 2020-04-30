import sys
sys.stdin = open('수들의 합.txt')

from itertools import permutations
from math import factorial as a

N, F = map(int, input().split())

fac = []
for i in range(N):
    fac.append(a(N-1)//(a(i)*a(N-1-i)))

for i in permutations(range(1,N+1)):
    ans = 0
    for j in range(N):
        ans += i[j]*fac[j]
    if ans == F:
        print(*i)
        break