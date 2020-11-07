arr = [0,5,4,0,6,0]

def babyGin():
    global flag
    chk = 0
    if arr[0] == arr[1] and arr[1] == arr[2]:
        chk += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        chk += 1

    if arr[0]+1 == arr[1] and arr[1] == arr[2]:
        chk += 1
    if arr[3]+1 == arr[4] and arr[4]+1 and arr[5]:
        chk += 1
    if chk == 2:
        flag = 1

def perm(n, k):
    if n == k:
        babyGin()
    for i in range(k, n):
        arr[k], arr[i] = arr[i], arr[k]
        perm(n, k + 1)
        arr[k], arr[i] = arr[i], arr[k]
flag = 0
perm(6, 0)

if flag:
    print("Baby-gin")
else:
    print("Not Baby-gin")