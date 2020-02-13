import sys
sys.stdin = open('농작물 수확하기.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input())))
    k = N//2
    cnt = 0
    for i in range(N):
        if k == 0:
            cnt += sum(matrix[i])
        else:
            cnt += sum(matrix[i][abs(k):-abs(k)])
        k -= 1

    print('#{} {}'.format(test_case, cnt))