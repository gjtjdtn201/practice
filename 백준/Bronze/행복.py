import sys
sys.stdin = open('행복.txt', 'r')

T = int(input())

st = list(map(int, input().split()))

st.sort()

print(st[-1] - st[0])