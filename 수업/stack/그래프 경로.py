import sys
sys.stdin = open("그래프 경로.txt", "r")

T = int(input())

for test_case in range(1, T+1):

    V, E = list(map(int,input().split()))

    a = [[] for i in range(V+1)]

    for i in range(E):
        nd1, nd2 = list(map(int, input().split()))
        a[nd1].append(nd2)

    st, ed = list(map(int, input().split()))

    stack = [st]
    visit = []
    ans = 0
    while stack:
        n = stack.pop()
        for i in a[n]:
            if ed in a[i]:
                ans = 1
                break
            elif i not in visit:
                stack.append(i)
        if n not in visit:
            visit.append(n)

    print('#{} {}'.format(test_case, ans))