import sys
sys.stdin = open('네트워크 연결.txt')

import sys
# input = sys.stdin.readline

for tc in range(int(input())):
    m, c, i = map(int, input().split())
    program = list(input().rstrip().split())
    A = list(input().rstrip().split())
    arr = [0]*m