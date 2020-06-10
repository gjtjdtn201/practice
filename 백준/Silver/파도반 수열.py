import sys
sys.stdin = open('파도반 수열.txt')

for tc in range(int(input())):
    N = int(input())
    P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(11, N+1):
        P.append(P[i-3]+P[i-2])
    print(P[N])