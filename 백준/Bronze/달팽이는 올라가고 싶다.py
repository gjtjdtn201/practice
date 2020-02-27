import sys
sys.stdin = open('달팽이는 올라가고 싶다.txt', 'r')

A, B, V = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    V -= A
    if V <= 0:
        break
    V += B
print(cnt)