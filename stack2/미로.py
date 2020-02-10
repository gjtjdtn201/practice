import sys
sys.stdin = open("미로.txt", "r")

def safe(y, x):
    return N > y >= 0 and N > x >= 0 and(Maze[y][x] == 0 or Maze[y][x] == 3)

def DFS(sty, stx):
    global ans
    if Maze[sty][stx] == 3:
        ans = 1
        return

    visit.append((sty, stx))
    for i in range(4):
        Py = sty + dy[i]
        Px = stx + dx[i]
        if (Py, Px) not in visit and safe(Py, Px):
            DFS(Py, Px)


T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    Maze =[]
    for i in range(N):
        Maze.append(list(map(int,input())))

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                sty, stx = y, x

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    ans = 0
    visit =[]
    DFS(sty,stx)
    print('#{} {}'.format(test_case, ans))