import sys
sys.stdin = open('버블 정렬.txt')

import heapq

N, K = map(int, input().split())
a = list(map(int, input().split()))
heap = a[:K]
heapq.heapify(heap)

for i in range(K, N):
    if heap[0] > a[i]:
        print(a[i], end=' ')
    else:
        print(heapq.heappop(heap), end=' ')
        heapq.heappush(heap, a[i])
while heap:
    print(heapq.heappop(heap), end=' ')