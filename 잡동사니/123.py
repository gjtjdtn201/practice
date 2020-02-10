def primes(val):
    a = [False, False]+[True]*(val-1)
    PN = []
    for i in range(2,val+1):
        if a[i] == True:
            PN.append(i)
            for j in range(i*2,val,i):
                a[j] = False
    return PN

print(primes(5))