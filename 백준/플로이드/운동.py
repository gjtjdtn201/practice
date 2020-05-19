import sys
sys.stdin = open('운동.txt')

V, E = map(int, input().split())
matrix = [[float('inf')]*V for _ in range(V)]

for i in range(E):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = min(matrix[a-1][b-1], c)

for k in range(V):
    for i in range(V):
        for j in range(V):
            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
ans = float('inf')
for i in range(V):
    ans = min(matrix[i][i], ans)
print(-1 if ans == float('inf') else ans)