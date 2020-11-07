import sys
sys.stdin = open('Ladder2.txt','r')

for test_case in range(10):
    T = int(input())
    ladder = []
    # 최솟값을 구하기 위해서 임의로 큰 값을 넣어둠
    minval = 9999

    # 사다리 받아오기
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    # i를 사다리의 첫번째 항을 돌게끔 반복하고 탐색시작
    for i in range(100):
        if ladder[0][i] == 1:

            # 카운트는 탐색을 한번 진행할때 마다 올라감 이경우 아래 한칸 내려갔다고 가정해서 1로 시작
            cnt = 1
            x = i
            y = 1

            # 체크는 현재 위치의 방향을 알기 위해서 설정함
            chk = 0

            # y가 끝에 도달하면 끝나게 while을 사용함
            while y < 99:

                # 방향은 순서대로 1.아래로 내려가기, 2.오른쪽 탐색, 3.왼쪽탐색
                direction = [(1, 0), (0, 1), (0, -1)]
                y += direction[chk][0]
                x += direction[chk][1]

                # 탐색 한칸 가고 카운트를 1 증가시킴
                cnt += 1

                # 조건이 벽이 아니거나 1일경우 방향을 지정함
                if x + 1 < 100 and chk != 2 and ladder[y][x + 1] == 1:
                    chk = 1
                elif x - 1 >= 0 and chk != 1 and ladder[y][x - 1] == 1:
                    chk = 2
                # 아래가 1이면 아래로 내려감
                elif y + 1 < 100 and ladder[y + 1][x] == 1:
                    chk = 0

        # while 문이 끝나고 카운트가 기존 후보보다 작으면 카운트를 작은것으로 바꾸고 답을 후보로 바꿈
        if minval > cnt:
            minval = cnt
            ans = i

    print('#{} {}'.format(T, ans))