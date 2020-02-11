import sys
sys.stdin = open('의석이의 세로로 말해요.txt', 'r')

T = int(input())

for test_case in range(1,1+T):
    a = []
    b = []
    for i in range(5):
        word = list(input())
        a.append(word)
        b.append(len(word))
    for i in a:
        while len(i) != max(b):
            i.append(' ')
    a = list(zip(*a))
    c = ''
    for i in a:
        c += ''.join(i)
    c = c.replace(' ', '')
    print('#{} {}'.format(test_case, c))