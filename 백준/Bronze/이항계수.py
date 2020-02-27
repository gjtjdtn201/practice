import sys
sys.stdin = open('이항계수.txt', 'r')

def fact(n):
    if fac[n] != 0:
        return fac[n]
    else:
        ans = 1
        for i in range(2, n+1):
            ans *= i
            fac[i] = ans
    return fac[n]
a, b = map(int, input().split())
fac = [1]*2 + [0] * (a-1)
print(fact(a) // fact(b) // fact(a -b))