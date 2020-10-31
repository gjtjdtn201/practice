from itertools import permutations
from collections import deque

def oper(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    else:
        return x*y


def solution(expression):
    answer = 0
    num = []
    operator = []
    numchk = ''
    for i in expression:
        if i.isdecimal():
            numchk += i
        else:
            if i not in operator:
                operator.append(i)
            num.append(int(numchk))
            num.append(i)
            numchk = ''
    num.append(int(numchk))
    for i in permutations(range(len(operator))):
        numstack = deque(num)
        for j in i:
            tmp = []
            while numstack:
                a = numstack.popleft()
                if a in operator:
                    if operator.index(a) == j:
                        tmp.append(oper(tmp.pop(), numstack.popleft(), a))
                        continue
                tmp.append(a)
            numstack = deque(tmp)
        answer = max(abs(numstack[0]), answer)

    return answer


a = "100-200*300-500+20"
print(solution(a))