def stars(a):
    matrix = []
    for i in range(3 * len(a)):
        if i // len(a) == 1:
            matrix.append(a[i % len(a)] + " " * len(a) + a[i%len(a)])
        else:
            matrix.append(a[i % len(a)] * 3)
    return list(matrix)

star = ['***','* *','***']
T = int(input())
k = 0
while T != 3:
    T = T // 3
    k += 1
for i in range(k):
    star = stars(star)
for i in star:
    print(i)