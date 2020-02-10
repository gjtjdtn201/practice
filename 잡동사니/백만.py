import sys
sys.stdin = open("input2.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    max = 0
    b = 0
    for i in range(N - 1, -1, -1):
        if max < data[i]:
            max = data[i]
        b += max - data[i]

    print('#{} {}'.format(test_case, b))
