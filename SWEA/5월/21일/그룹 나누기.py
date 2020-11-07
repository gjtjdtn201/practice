import sys
sys.stdin = open('그룹 나누기.txt')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    p = [x for x in range(N+1)]
    for i in range(M):
        a = find_set(A[i*2])
        b = find_set(A[i*2+1])
        p[b] = a
    res = []
    for i in range(N+1):
        res.append(find_set(i))
    ans = len(set(res))-1
    print('#{} {}'.format(tc, ans))