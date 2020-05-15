import sys
sys.stdin = open('이중 우선순위 큐.txt')

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    maxh, minh = [], []
    N = int(input())
    visit = [False]*N
    for i in range(N):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(maxh, (-b, i))
            heapq.heappush(minh, (b, i))
            visit[i] = True
        else:
            if b == -1:
                while minh and not visit[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    visit[heapq.heappop(minh)[1]] = False
            else:
                while maxh and not visit[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    visit[heapq.heappop(maxh)[1]] = False
    while minh and not visit[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not visit[maxh[0][1]]:
        heapq.heappop(maxh)
    print(-heapq.heappop(maxh)[0], heapq.heappop(minh)[0]) if minh else print('EMPTY')
