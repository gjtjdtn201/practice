import sys
sys.stdin = open('효율적인 해킹.txt', 'r')

from collections import deque

n, m = map(int, input().split())
def bfs(s):
    queue = deque()
    queue.append(s)
    visited = [False] * (n + 1)
    visited[s] = True
    count = 1
    while queue:
        node = queue.popleft()
        for next in myGraph[node]:
            if not (visited[next]):
                visited[next] = True
                queue.append(next)
                count += 1

    return count


myGraph = [[] for _ in range(n + 1)]
for _ in range(m):
    A, B = map(int, input().split())
    myGraph[B].append(A)

maxValue = -1
result = []
for i in range(1, len(myGraph)):
    c = bfs(i)
    if c > maxValue:
        result = [i]
        maxValue = c
    elif c == maxValue:
        result.append(i)
        maxValue = c

for e in result:
    print(e, end=' ')