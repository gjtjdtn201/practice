import sys
sys.stdin = open("괄호검사.txt", "r")

def my_func(s):
    a = []
    for i in s:
        if i == '{' or i == '(':
            a.append(i)
            continue
        if i == '}' or i == ')':
            if a == [] :
                return 0
            elif a[-1] == '{' and i == '}':
                a.pop()
            elif a[-1] == '(' and i == ')':
                a.pop()
            else:
                return 0
    if a:
        return 0
    return 1



T = int(input())

for test_case in range(1, T+1):
    s = input()

    print('#{} {}'.format(test_case, my_func(s)))