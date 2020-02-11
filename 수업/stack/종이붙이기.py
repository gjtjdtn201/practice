import sys
sys.stdin = open("종이붙이기.txt", "r")

def fib(num):
    if num < 2:
        return num
    else:
        if num % 2 == 0:
            return fib(num - 1)*2 + 1
        return fib(num - 1)*2 - 1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ans = fib(N//10)

    print('#{} {}'.format(test_case, ans))