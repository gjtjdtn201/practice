d = list(range(10000))

for i in range(10000):
    cnt = i
    for j in str(i):
        cnt += int(j)
    if cnt < 10000:
        d[cnt] = 0
for k in d:
    if k:
        print(k)