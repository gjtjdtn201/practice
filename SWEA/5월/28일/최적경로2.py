import sys
sys.stdin = open('최적경로.txt')

def perm(n,k,prev,d):
    global Min
    if d > Min:
        return

    if n==k:
        d += (abs(cords[prev][0]-cords[N+1][0])+abs(cords[prev][1]-cords[N+1][1]))
        Min = min(d, Min)
        return

    for i in range(1,1+k):
        if not v[i]:
            p[n] = i
            v[i] = 1
            perm(n+1,k,i,d+(abs(cords[prev][0]-cords[i][0])+abs(cords[prev][1]-cords[i][1])))
            v[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int,input().split()))
    cords = []
    memoi = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        cords.append([temp[2*i],temp[2*i+1]])
    Min = 100000000000000
    p = [0] * (N)
    v = [0] * (N+1)
    perm(0,N,0,0)

    print("#{} {}".format(tc,Min))