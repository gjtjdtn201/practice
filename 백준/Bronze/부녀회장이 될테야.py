import sys
sys.stdin = open('부녀회장이 될테야.txt', 'r')

a = [list(range(1, 15)) for _ in range(15)]
for i in range(1, 15):
    for j in range(1, 14):
        a[i][j] = a[i - 1][j] + a[i][j - 1]

T = int(input())

for test_case in range(T):
    k = int(input())
    n = int(input())
    print(a[k][n-1])