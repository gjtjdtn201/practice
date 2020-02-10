import sys
sys.stdin = open("새샘이와 세 소수.txt", "r")

def prime_list(n):
    a = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    PN = prime_list(N)
    cnt = [0 for i in PN for j in PN for k in PN if i+j+k == N and i<=j and j<=k]



    print('#{} {}'.format(test_case, len(cnt)))