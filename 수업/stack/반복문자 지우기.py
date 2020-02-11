import sys
sys.stdin = open("반복문자 지우기.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    sl = list(input())

    stack = [0]

    for i in sl:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print('#{} {}'.format(test_case, len(stack)-1))