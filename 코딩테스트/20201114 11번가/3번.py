import fractions

X = [7,4,4,7,1,2]
Y = [8,4,4,8,1,2]
mydict = {}
N = len(X)
for i in range(N):
    num = fractions.Fraction(X[i], Y[i])
    if mydict.get(num):
        mydict[num] += 1
    else:
        mydict[num] = 1
ans = max(mydict.values())
print(mydict)
print(ans)