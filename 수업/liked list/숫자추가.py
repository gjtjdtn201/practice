import sys
sys.stdin = open("숫자추가.txt", 'r')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    al = list(map(int, input().split()))

    for i in range(M):
        idx, num = map(int, input().split())
        al.insert(idx, num)
    print('#{} {}'.format(tc, al[L]))