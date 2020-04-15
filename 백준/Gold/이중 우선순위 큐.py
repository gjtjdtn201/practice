import sys
sys.stdin = open('이중 우선순위 큐.txt')

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h = []
    for i in range(int(input())):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(h, b)
        else:
            if h:
                if b == -1:
                    heapq.heappop(h)
                else:
                    h.remove(max(h))
    print(max(h), min(h)) if h else print('EMPTY')