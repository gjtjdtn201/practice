import sys
sys.stdin = open('달리기.txt', 'r')

from itertools import permutations

T = int(input())

for test_case in range(1, T+1):
    # N은 사람 수, M은 테스트 수
    N, M = map(int, input().split())
    al = bl = []
    for i in range(M):
        a,b = map(int, input().split())
        al.append(a)
        bl.append(b)
    pos = list(permutations(range(1, N+1)))

    # for i in pos:
    #     if a[]
    print(pos)