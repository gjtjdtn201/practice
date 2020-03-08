import sys
sys.stdin = open('AC.txt')

import sys
input = sys.stdin.readline
from collections import deque

for tc in range(int(input())):
    p = input().rstrip()
    n = int(input())
    a = input().rstrip()
    b = deque()
    word = ''
    for i in a:
        if i.isdecimal():
            word += i
        elif i == ',' or i == ']':
            if word.isdecimal():
                b.append(word)
                word = ''
    chk = 0
    for i in p:
        if i == 'R':
            if chk == 0:
                chk = 1
            else:
                chk = 0
        elif i == 'D':
            try:
                if chk == 1:
                    b.pop()
                else:
                    b.popleft()
            except IndexError:
                b = 'error'
                break
    if b == 'error':
        print(b)
    elif chk == 1:
        b.reverse()
        print('[',end='')
        print(','.join(b),end='')
        print(']')
    else:
        print('[', end='')
        print(','.join(b), end='')
        print(']')