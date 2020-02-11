N = int(input())

cnt = 0

if N - 9*len(str(N)) < 0:
    ans = 0
else:
    for i in range(N - 9*len(str(N)), N):
        cnt = 0
        for j in str(i):
            cnt += int(j)
        if cnt + i == N:
            ans = i
            break
    else:
        ans = 0
print(ans)