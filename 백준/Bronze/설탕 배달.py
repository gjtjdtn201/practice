n = int(input())
ans = 0

while n > 0:
    if n % 5 != 0:
        n -= 3
        if n < 0:
            ans = -1
            break
        ans += 1
    elif n % 5 == 0:
        ans += 1
        n -= 5
    elif n % 5 != 0 and n % 3 != 0:
        ans -= 1
print(ans)