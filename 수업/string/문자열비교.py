import sys
sys.stdin = open("문자열비교.txt", "r")

T = int(input())

for i in range(1,T+1):
    m = input()
    n = input()
    ans = 0
    if m in n:
        ans +=1

    print(f'#{i} {ans}')