import sys
sys.stdin = open("구간합input.txt", "r")

T = int(input())

for i in range(1, T + 1):

    # N 에 총 숫자열의 갯수, M 에 구간의 수 받음
    N, M = list(map(int,input().split()))

    # TestList TL에 숫자열을 리스트로 받음
    TL = list(map(int,input().split()))

    a = 0

    # 초기 min, max 값을 받기 위해서 첫번째 항을 받음
    for z in range(M):
        a += TL[z]
        minl = maxl = a

    # k를 한개씩 증가시키면서 크면 maxl 값에 작으면 minl 값에 저장
    for k in range(N-M):
        a = 0
        for z in range(M):
            a += TL[z+k+1]
        if maxl < a:
            maxl = a
        elif minl > a:
            minl = a

    print(f'#{i} {maxl-minl}')