import sys
sys.stdin = open('구간 합 구하기.txt', 'r')

import sys
# input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
for i in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b-1] = c
    else:
        print(sum(arr[b-1:c]))