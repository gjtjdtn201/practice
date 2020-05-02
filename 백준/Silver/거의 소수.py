A, B = map(int, input().split())

a = [False, False] + [True]*(10**7+1)
for i in range(2, 10**7+1):
    if a[i]:
        for j in range(2*i, 10**7+1, i):
            a[j] = False

ans = 0
maxp = 100
for i in range(2,10**7+1):
    if a[i]:
        n = 2
        now = i*i
        while n <= maxp and now <= B:
            if now >= A:
                ans += 1
            now *= i
            n += 1
        maxp = n-1
        if maxp == 1:
            break
print(ans)
