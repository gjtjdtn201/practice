# a =[[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

a = [[0 for j in range(5)] for i in range(5)]
X = 5
num = list(range(1,26))
delta = 1
index = 0
i, j = 0, -1
while X > 0:
    for k in range(X):
        j += delta
        a[i][j] = num[index]
        index += 1
    X -= 1

    if X == 0:
         break

    for k in range(X):
        i += delta
        a[i][j] = num[index]
        index += 1
    delta = -delta

print(a)