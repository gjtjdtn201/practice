n, k = map(int, input().split())

d = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        d.append(i)
        if i != n//i:
            d.append(n//i)
d.sort()

if len(d) < k:
    ans = 0
else:
    ans = d[k-1]

print(ans)