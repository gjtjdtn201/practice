import sys
sys.stdin = open("minmaxinput.txt", "r")

def case(value):
    if 5 <= value <= 1000:
        N = input()
        b = list(map(int, N.split()))
        maxval = b[0]
        minval = b[0]
        for i in b:
            if i > maxval:
                maxval = i
            if i < minval:
                minval = i

        return maxval - minval
    else:
        print("5 이상 1000 이하의 수를 입력하세요")
        return

T = int(input())

if 1<= T <= 50:
    for i in range(1, T+1):
        Ans = case(int(input()))
        print(f'#{i} {Ans}')
else:
    print('1 이상 50 이하의 수를 입력하세요')