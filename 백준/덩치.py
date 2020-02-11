import sys
sys.stdin = open('덩치.txt', 'r')

T = int(input())
a = []
b = [1] * T
for i in range(T):
    x, y = map(int, input().split())
    a.append((x,y))
for i in range(T):
    for j in range(T):
        if i == j:
            continue
        elif a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            b[i] += 1
b = tuple(b)
print(*b)

