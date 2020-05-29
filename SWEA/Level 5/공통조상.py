import sys
sys.stdin = open('공통조상.txt')

def order(n):
    global cnt
    if n != 0:
        cnt += 1
        order(tree[n][0])
        order(tree[n][1])

def find(current, parents):
    if current != 0:
        t = tree[current][2]
        if t in parents:
            return t
        parents.append(t)
        return find(t, parents)
    return parents

for tc in range(1, int(input())+1):
    V, E, n1, n2 = map(int, input().split())
    A = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(V+1)]
    cnt = 0
    for i in range(0, len(A)-1, 2):
        if tree[A[i]][0]:
            tree[A[i]][1] = A[i+1]
        else:
            tree[A[i]][0] = A[i+1]
        tree[A[i+1]][2] = A[i]
    B = find(n2, find(n1, []))
    order(B)
    print('#{} {} {}'.format(tc, B, cnt))
