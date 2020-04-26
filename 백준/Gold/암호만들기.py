import sys
sys.stdin = open('암호만들기.txt')

from itertools import combinations

L, C = map(int, input().split())
a = list(input().split())
a.sort()
b = ['a','e','i','o','u']
for words in combinations(a, L):
    chk1, chk2 = 0, 0
    for word in words:
        if word in b:
            chk1 = 1
        else:
            chk2 += 1
    if chk1 == 1 and chk2 >= 2:
        for i in words:
            print(i, end='')
        print()