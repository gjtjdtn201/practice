c = [1,2,3]
a = set(c)
b = set(c)

a = a - b

if a == set():
    print('hi')
print(a)