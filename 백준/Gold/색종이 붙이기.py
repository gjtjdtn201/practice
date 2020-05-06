import sys
sys.stdin = open('색종이 붙이기.txt')

def coverchk(y, x, ny, nx):
    for yy in range(y, ny):
        for xx in range(x, nx):
            if matrix[yy][xx] == 0:
                return False
    return True

def solution(st, depth):
    global ans, total
    if depth >= ans:
        return
    if total == 0:
        ans = min(ans, depth)
        return
    for i in range(st, 100):
        y = i // 10
        x = i % 10
        if matrix[y][x]:
            for size in range(5, 0, -1):
                if paper[size]:
                    ny = size + y
                    nx = size + x
                    if ny <= 10 and nx <= 10:
                        if coverchk(y, x, ny, nx):
                            paper[size] -= 1
                            total -= size**2
                            for yy in range(y, ny):
                                for xx in range(x, nx):
                                    matrix[yy][xx] = 0
                            solution(i+1, depth+1)
                            paper[size] += 1
                            total += size**2
                            for yy in range(y, ny):
                                for xx in range(x, nx):
                                    matrix[yy][xx] = 1
            return

matrix = [list(map(int, input().split())) for _ in range(10)]

paper = [0, 5, 5, 5, 5, 5]
ans = 26
total = sum(sum(i) for i in matrix)
solution(0, 0)
print(-1 if ans == 26 else ans)