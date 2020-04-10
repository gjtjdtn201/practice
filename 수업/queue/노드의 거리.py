import sys
sys.stdin = open('노드의 거리.txt', 'r')

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    tree = [[] for num in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    S, G = map(int, input().split())

    queue = deque()
    queue.append(S)
    visit = [0]*(V+1)
    visit[S] = 1
    ans = 0
    while queue:
        n = queue.popleft()
        if n == G:
            ans = visit[G] - 1
            break
        for i in tree[n]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = visit[n] + 1
    print('#{} {}'.format(test_case, ans))