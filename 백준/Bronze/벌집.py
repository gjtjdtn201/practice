T = int(input())
ans = 1
if T > 1:
    cnt = ans = 0
    while True:
        ans += 1
        if 6 * (cnt)  + 1 >= T:
            break
        cnt += ans
print(ans)