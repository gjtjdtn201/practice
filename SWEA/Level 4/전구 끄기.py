import sys
sys.stdin = open('전구 끄기.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(m):
        a, b = int(input())
