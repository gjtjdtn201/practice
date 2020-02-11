import sys
sys.stdin = open('블랙잭.txt', 'r')

from itertools import combinations

N, M = map(int, input().split())

word = list(map(int, input().split()))

ans = combinations(word,3)
res = 0
for i in ans:
    a = sum(i)
    if a <= M:
       if res < a:
           res = a

print(res)
