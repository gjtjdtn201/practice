import sys
sys.stdin = open('슈퍼마리오.txt', 'r')

T = 10
cnt = 0
for i in range(10):
    MR = int(input())
    if abs(100 - (cnt + MR)) <= abs(100 - cnt):
        cnt = cnt + MR
    else:
        break
print(cnt)