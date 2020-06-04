import sys
sys.stdin = open('상원이의 생일파티.txt')

from collections import deque

def BFS():
    q = deque()
    q.append((1, 0))
    visit = [0] * (N + 1)
    visit[1] = 1
    cnt = 0
    while q:
        node, depth = q.popleft()
        if depth < 2:
            for i in tree[node]:
                if not visit[i]:
                    q.append((i, depth + 1))
                    visit[i] = 1
                    cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    print('#{} {}'.format(tc, BFS()))