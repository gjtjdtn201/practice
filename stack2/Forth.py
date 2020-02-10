import sys
sys.stdin = open("Forth.txt", "r")

def cal(val1,val2,oper):
    if oper == '+':
        return val2 + val1
    elif oper == '-':
        return val2 - val1
    elif oper == '*':
        return val2 * val1
    else:
        return val2 // val1

T = int(input())

for test_case in range(1, T+1):
    sl = list(input().split())
    ans = 0
    stack = []
    for i in sl:
        if i == '.':
            break
        elif i.isdecimal():
            stack.append(int(i))
        elif len(stack) < 2:
            stack.append('error')
            break
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(cal(a,b,i))

    if len(stack) == 1:
        ans = stack.pop()
    else:
        ans = 'error'

    print('#{} {}'.format(test_case, ans))