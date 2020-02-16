import sys
sys.stdin = open('성수의 비밀번호 공격.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    M, N = map(int, input().split())