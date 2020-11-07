import sys
sys.stdin = open('작업순서.txt', 'r')

for test_case in range(1, 11):
    V, E = map(int, input().split())
    link = list(map(int, input().split()))
    tree = [[] for _ in range(V+1)]
    result = []
    visit = [False]*(V+1)
    for i in range(0, len(link), 2):
        tree[link[i+1]].append(link[i])
    while len(result) < V:
        for i in range(1, V+1):
            if tree[i] == [] and not visit[i]:
                result.append(i)
                visit[i] = True
                for j in range(1, V+1):
                    if i in tree[j]:
                        tree[j].remove(i)

    print('#{} '.format(test_case), end='')
    print(*result)