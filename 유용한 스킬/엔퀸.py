N = int(input())

matrix = [0] * N

def findQueen(x):
    for i in range(x):
        if matrix[x] == matrix[i] or abs(matrix[x] - matrix[i]) == abs(x - i):
            return False
    return True


def setQueen(cnt):
    global ans

    if cnt == N:
        ans += 1
    else:
        for i in range(N):
            matrix[cnt] = i
            if findQueen(cnt):
                setQueen(cnt + 1)

ans = 0
setQueen(0)

print(ans)