import sys
sys.stdin = open("전기버스input.txt", "r")

def EB(K, N):
    EC = list(map(int, input().split()))
    pos = 0
    Ans = 0

    #현재 위치가 도착지점 N까지 가지않을경우 반복함
    while pos < N:
        Ans, pos = MP(Ans, pos, K, EC)
        pos += K

        # 충전 불가능을 받았을경우 강제로 while뮨을 깨고 0을 리턴
        if Ans == 0:
            break
    return Ans

# 포지션이 현재 위치한 곳이 충전소인지 확인하는 함수
def MP(Ans, pos, K, EC):

    for i in range(K):

        # 출발 지점일 경우 K만큼 출발하라는 것
        if pos == 0:
            pos += K

        # 현재 포지션에 충전소가 있다면 for문을 깨고 리턴하기 위함
        elif pos in EC:
            Ans += 1
            break

        # 충전소가 없으면 현재 포지션에서 뒤로가는 작업
        else:
            pos += -1

    # for else 문을 사용하여 원래 위치로 왔을경우 더이상 충전 불가능 0 리턴
    else:
        Ans = 0

    return Ans, pos

T = int(input())

if 1 <= T <= 50:
    for i in range(1, T + 1):
        K, N, M = list(map(int, input().split()))
        Ans = EB(K, N)
        print(f'#{i} {Ans}')
else:
    print('1 이상 50 이하의 수를 입력하세요.')