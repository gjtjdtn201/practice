import sys
sys.stdin = open('이차원 배열과 연산.txt')

r, c, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(3)]
row, col = 3, 3
cnt = 0
while cnt <= 100:
    row, col = len(matrix), len(matrix[0])
    if r <= row and c <= col and matrix[r-1][c-1] == k:
        print(cnt)
        break
    chk2 = 0
    if row < col:
        chk = col
        chk2 = 1
        matrix = list(zip(*matrix))
    else:
        chk = row
    ml = 0
    for i in range(chk):
        new = {}
        for j in matrix[i]:
            if j == 0:
                continue
            if not new.get(j):
                new[j] = 1
            else:
                new[j] += 1
        b = []
        for y, x in new.items():
            b.append((y, x))
        b.sort(key=lambda x: (x[1], x[0]))
        matrix[i] = []
        for z in b:
            matrix[i].extend(z)
            ml = max(ml, len(matrix[i]))
    for i in range(chk):
        for _ in range(ml-len(matrix[i])):
            matrix[i].append(0)
    if chk2:
        matrix = list(zip(*matrix))
    cnt += 1
else:
    print(-1)