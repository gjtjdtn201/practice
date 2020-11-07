import sys
sys.stdin = open('회문2.txt', 'r')

def PL(lista):
    for N in range(100, 0, -1):
        for i in range(100 - N + 1):
            if lista[i:N + i] == lista[i:N + i][::-1]:
                return N
T = 10
for test_case in range(1, T+1):
    TC = int(input())
    matrix = []
    ans = 0
    for _ in range(100):
        word = list(input())
        matrix.append(word)
        a = PL(word)
        if ans < a: ans = a
    matrix = list(zip(*matrix))
    for j in matrix:
        a = PL(j)
        if ans < a: ans = a
    print('#{} {}'.format(test_case, ans))