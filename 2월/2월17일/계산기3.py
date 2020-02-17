import sys
sys.stdin = open("계산기3.txt", "r")

def cal(val1, val2, oper):
    if oper == '+':
        return val2 + val1
    elif oper == '-':
        return val2 - val1
    elif oper == '*':
        return val2 * val1
    else:
        return val2 // val1

def isp(val):
    if val == '(':
        return 0
    elif val == '+' or val == '-':
        return 1
    elif val == '*' or val == '/':
        return 2

def icp(val):
    if val == '(':
        return 3
    elif val == '+' or val == '-':
        return 1
    elif val == '*' or val == '/':
        return 2

for test_case in range(1, 11):
    T = int(input())
    word = list(input())
    sl = []
    stack = []
    for i in word:
        if i.isdecimal():
            sl.append(i)
        elif stack == []:
            stack.append(i)
        elif i == ')':
            while True:
                n = stack.pop()
                if n == '(':
                    break
                sl.append(n)

        elif isp(stack[-1]) < icp(i):
            stack.append(i)
        else:
            while True:
                n = stack.pop()
                if isp(n) < icp(i):
                    stack.append(n)
                    stack.append(i)
                    break
                sl.append(n)
    ans = 0
    for i in sl:
        if i.isdecimal():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(cal(a, b, i))
    if len(stack) == 1:
        ans = stack.pop()

    print('#{} {}'.format(test_case, ans))