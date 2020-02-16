import sys
sys.stdin = open('스타트와 링크.txt', 'r')

from itertools import combinations

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

a = list(combinations(range(1, N+1), N//2))
ans = 9999
for i in a[:len(a)//2]:
    cnt = cnt2 = 0
    num = list(range(1, N + 1))
    for j in i:
        num.remove(j)
        for k in i:
            cnt2 += matrix[j-1][k-1]
    for j in num:
        for k in num:
            cnt += matrix[j-1][k-1]
    if abs(cnt - cnt2) < ans:
        ans = abs(cnt - cnt2)
print(ans)