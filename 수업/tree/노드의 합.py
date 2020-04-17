import sys
sys.stdin = open('노드의 합.txt')

def find(num):
    if num*2 + 1 <= N:
        tree[num] = find(num*2) + find(num*2+1)
    elif num*2 <= N:
        tree[num] = find(num*2)
    return tree[num]
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    ans = find(L)
    print('#{0} {1}'.format(tc, ans))