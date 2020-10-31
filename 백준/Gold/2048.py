import sys
sys.stdin = open('2048.txt')

def solution(n, matrix):
    global ans
    if n > 5:
        for i in matrix:
            if ans < max(i):
                ans = max(i)
        return
    for dist in range(4):
        matrix2 = list([0 for _ in range(N)] for __ in range(N))
        cnt = 0
        if dist < 2:
            if dist == 0:
                start, end, num = 0, N, 1
            else:
                start, end, num = N-1, -1, -1
            for x in range(N):
                chk, q = 0, []
                for y in range(start, end, num):
                    if matrix[y][x] == 0:
                        if y == end-1 or (dist == 1 and y == 0):
                            q.append(chk)
                        continue
                    if chk == 0:
                        chk = matrix[y][x]
                        if y == end-1 or (dist == 1 and y == 0):
                            q.append(chk)
                    elif chk != matrix[y][x]:
                        q.append(chk)
                        chk = matrix[y][x]
                        if y == end-1 or (dist == 1 and y == 0):
                            q.append(chk)
                    else:
                        q.append(chk*2)
                        if cnt < chk*2:
                            cnt = chk*2
                        chk = 0
                if dist == 0:
                    for z in range(len(q)):
                        matrix2[z][x] = q[z]
                else:
                    n2 = 0
                    for z in range(len(q)-1, -1, -1):
                        matrix2[N-n2-1][x] = q[n2]
                        n2 += 1
        else:
            if dist == 2:
                start, end, num = 0, N, 1
            else:
                start, end, num = N-1, -1, -1
            for y in range(N):
                chk, q = 0, []
                for x in range(start, end, num):
                    if matrix[y][x] == 0:
                        if x == end-1 or (dist == 3 and x == 0):
                            q.append(chk)
                        continue
                    if chk == 0:
                        chk = matrix[y][x]
                        if x == end-1 or (dist == 3 and x == 0):
                            q.append(chk)
                    elif chk != matrix[y][x]:
                        q.append(chk)
                        chk = matrix[y][x]
                        if x == end-1 or (dist == 3 and x == 0):
                            q.append(chk)
                    else:
                        q.append(chk*2)
                        if cnt < chk*2:
                            cnt = chk*2
                        chk = 0
                if dist == 2:
                    for z in range(len(q)):
                        matrix2[y][z] = q[z]
                else:
                    n2 = 0
                    for z in range(len(q)-1, -1, -1):
                        matrix2[y][N-n2-1] = q[n2]
                        n2 += 1

        solution(n+1, matrix2)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = 2

# 1,2,3,4 위, 아래, 왼, 오른

solution(1, matrix)
print(ans)