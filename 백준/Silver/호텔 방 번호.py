import sys
sys.stdin = open('호텔 방 번호.txt')

while True:
    try:
        a, b = map(int, input().split())
        cnt = 0
        while a <= b:
            chk = {}
            for i in str(a):
                if not chk.get(i):
                    chk[i] = 1
                else:
                    break
            else:
                cnt += 1
            a += 1
        print(cnt)
    except EOFError:
        break