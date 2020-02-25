import sys
sys.stdin = open('디저트 카페.txt', 'r')

def DFS(i, j, chk, visit):
    global ans
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if chk == 4:
        return
    if i == x and j == y and len(visit) != 0:
        if ans < len(visit):
            ans = len(visit)
        return
    if matrix[i][j] in visit:
        return

    DFS(i + dy[chk], j + dx[chk], chk, visit + [matrix[i][j]])
    DFS(i + dy[chk], j + dx[chk], chk + 1, visit + [matrix[i][j]])

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    dy = [1, 1, -1, -1]
    dx = [1, -1, -1, 1]

    ans = -1
    for i in range(N-2):
        for j in range(1, N-1):
            x, y = i, j
            DFS(i, j, 0, [])
    print('#{} {}'.format(test_case, ans))