import sys
sys.stdin = open('재미있는 오셀로 게임.txt', 'r')

def safe(x,y):
    return N > x >= 0 and N > y >= 0


def CC(A,B,C,dx,dy):
        tmp = []
        for i in range(N):
            A += dx
            B += dy
            if safe(A, B):
                tmp.append((A, B))
                if OS[A][B] == 0:
                    break
                elif OS[A][B] == C:
                    while tmp:
                        n = tmp.pop()
                        OS[n[0]][n[1]] = C
                    break

T = int(input())

for test_case in range(1,1+T):
    N, M = map(int, input().split())
    OS = [[0 for x in range(N)] for y in range(N)]
    # 1이 블랙 2가 화이트
    for i in range(2):
        OS[N//2-i][N//2-1+i] = 1
        OS[N//2-i][N//2-i] = 2

    dy = [1,-1,0,0,1,-1,-1,1]
    dx = [0,0,1,-1,1,-1,1,-1]

    # A : x축 B : y축 C : 돌색깔
    for i in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        OS[A][B] = C
        for j in range(8):
            CC(A, B, C, dy[j], dx[j])
    black = 0
    white = 0
    for i in OS:
        black += i.count(1)
        white += i.count(2)

    print('#{} {} {}'.format(test_case, black, white))