import sys
sys.stdin = open('수 정렬하기2.txt', 'r')

import sys
input = sys.stdin.readline

a = [int(input())for i in range(int(input()))]
for i in sorted(a):print(i)