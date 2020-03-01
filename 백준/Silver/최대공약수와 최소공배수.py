import sys
sys.stdin = open('최대공약수와 최소공배수.txt', 'r')

def gcd(a, b):
    global ans
    if b == 0:
        ans = a
        return
    else:
        gcd(b, a % b)

n1, n2 = map(int, input().split())
gcd(n1, n2)
print(ans)
print(n1*n2//ans)
