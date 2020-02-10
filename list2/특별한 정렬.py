import sys
sys.stdin = open("특별한 정렬.txt", "r")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    ai.sort()
    a = []
    b = ''
    for j in range(len(ai)//2):
        a.append(ai[-j-1])
        a.append(ai[j])
    for k in a[:10]:
        b += str(k) + ' '
    b = b.rstrip(' ')
    print(f'#{i} {b}')