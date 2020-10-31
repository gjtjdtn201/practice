def solution(n, s, a, b, fares):
    answer = float('inf')
    matrix = [[float('inf')] * n for _ in range(n)]
    for i in fares:
        x, y, z = i
        matrix[x - 1][y - 1] = z
        matrix[y - 1][x - 1] = z
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == k:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
    for i in range(n):
        answer = min(answer, matrix[s-1][i] + matrix[i][a-1] + matrix[i][b-1])
    return answer

n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))