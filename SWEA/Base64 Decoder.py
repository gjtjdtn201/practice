import sys
sys.stdin = open("Base64 Decoder.txt","r")

def binary(a):
    b = bin(a)[2:]
    while len(b) < 6:
        b = '0' + b
    return b

T = int(input())

decoder = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')


for test_case in range(1, 1+T):
    ml = input()
    a = ''
    word = []
    for i in ml:
        a += binary(decoder.index(i))
    for i in range(0, len(a), 8):
        word.append(chr(int(a[i:i+8], 2)))

    print('#{} {}'.format(test_case, ''.join(word)))