import sys
sys.stdin = open('최소 힙.txt')

import heapq
import sys
input = sys.stdin.readline

h = []
for i in range(int(input())):
    a = int(input())
    if a != 0:
        heapq.heappush(h, a)
    else:
        try:
            print(heapq.heappop(h))
        except:
            print(0)