import sys
sys.stdin = open('스위치 켜고 끄기.txt','r')

T = int(input())
switch = list(map(int, input().split()))
N = int(input())
for _ in range(N):
    S, pos = map(int, input().split())
    if S == 1:
        for i in range(pos,len(switch),pos):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    elif S == 2:
        a = []
        a.append(pos)
        while True:
            0 <= (pos -1) and (pos+1) <= T



print(switch)
