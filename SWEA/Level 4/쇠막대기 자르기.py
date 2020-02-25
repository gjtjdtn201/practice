import sys
sys.stdin = open('쇠막대기 자르기.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    stick = list(input())
    stack = []
    cnt = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if stick[i-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))