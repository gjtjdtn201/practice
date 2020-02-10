import sys
sys.stdin = open("다솔이의 다이아몬드 장식.txt", "r")


def Aprint(word):
    a = ''
    print('.'+'.#..'*len(word))
    print('.'+'#.'*len(word)*2)
    print('#.', end='')
    for i in word:
        a += i + '.#.'
    print(a.rstrip('.'))
    print('.' + '#.' * len(word) * 2)
    print('.' + '.#..' * len(word))

T = int(input())

for test_case in range(1,T+1):
    word = input()
    Aprint(word)