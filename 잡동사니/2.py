def fib(n):
    global cnt,cnt1
    if n == 0:
        cnt += 1
    if n == 1:
        cnt1 +=1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
cnt = cnt1 =0
print(fib(4))
print(cnt,cnt1)