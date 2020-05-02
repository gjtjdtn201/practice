import sys
sys.stdin = open('소수의 연속합.txt')

N = int(input())

a = [False, False] + [True]*(N+1)
primes = []
for i in range(2, N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False
sum = ans = hi = lo = 0
c = len(primes)
while True:
    if sum >= N:
        sum -= primes[lo]
        lo += 1
    elif hi == c:
        break
    else:
        sum += primes[hi]
        hi += 1
    if sum == N:
        ans += 1
print(ans)