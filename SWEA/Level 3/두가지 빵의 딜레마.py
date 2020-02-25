import sys
sys.stdin = open('두가지 빵의 딜레마.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())

    print('#{} {}'.format(test_case, C // min(A,B)))