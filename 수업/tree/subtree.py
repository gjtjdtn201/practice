import sys
sys.stdin = open('subtree.txt')

def inorder(node):
    global result
    if node != 0:
        inorder(tree[node][0])
        result += 1
        inorder(tree[node][1])
for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    for i in range(E):
        n1 = data[i * 2]
        n2 = data[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
    result = 0
    inorder(N)
    print('#{0} {1}'.format(tc, result))