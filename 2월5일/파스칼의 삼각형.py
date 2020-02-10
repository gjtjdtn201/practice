import sys
sys.stdin = open("파스칼의 삼각형.txt", "r")

def pascal(n):
    a = [[] for _ in range(n)]
    for i in range(1, n+1):
        if i == 1:
            a[i-1].append(1)
        elif i == 2:
            a[i-1].extend([1,1])
        else:
            b = [1]
            for j in range(i-2):
                b.append(a[i-2][j]+a[i-2][j+1])
            b.append(1)
            a[i-1].extend(b)
    for k in a:
        b = ''
        for z in k:
            b += str(z) + ' '
        print(b.rstrip(' '))
T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    print('#{}'.format(test_case))
    pascal(N)