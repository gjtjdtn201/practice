import sys
sys.stdin = open('보호 필름.txt', 'r')

from itertools import combinations
from itertools import product


def check(cols) :
    for col in range(D - K + 1) :
        before = cols[col]
        for i in range(1, K) :
            if before != cols[col + i] :
                break
            before = cols[col + i]
        else :
            return True
    return False


def film() :
    for i in range(K) :
        for j in combinations(range(D), i) :
            for l in product([0, 1], repeat=i) :
                for cols in zip(*films) :
                    cols = list(cols)
                    for row in range(i) :
                        cols[j[row]] = l[row]
                    if not check(cols) :
                        break
                else :
                    return i
    return K


T = int(input())
for tc in range(1, T + 1) :
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    if K != 1 :
        print('#{0} {1}'.format(tc, film()))
    else :
        print('#{0} {1}'.format(tc, 0))
