import sys
sys.stdin = open('피자 굽기.txt', 'r')

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizzalist = list(enumerate(map(int, input().split())))
    pizza = deque()
    pizza.extend(pizzalist[:N])
    pizzalist = pizzalist[N:]
    while len(pizza) > 1:
        a, b = pizza.popleft()
        if b//2 == 0:
            if pizzalist:
                pizza.append(pizzalist.pop(0))
        else:
            pizza.append((a, b//2))

    print('#{} {}'.format(test_case, pizza[0][0]+1))