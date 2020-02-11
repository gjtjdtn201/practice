import sys
sys.stdin = open('창용 마을 무리의 개수.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    RS = [[] for num in range(N + 1)]
    for i in range(M):
        A, B = map(int, input().split())
        RS[A].append(B)
        RS[B].append(A)
    group = 0
    for i in range(1, N + 1):
        if RS[i] == []:
            continue
        else:
            stack = []
            stack.append(i)
            while stack:
                n = stack.pop()
                RS[0].append(n)
                if RS[n] == []:
                    continue
                else:
                    stack.extend(RS[n])
                    RS[n] = []
            group += 1

    cnt = N - len(set(RS[0]))
    print('#{} {}'.format(test_case, group + cnt))