import sys
sys.stdin = open("숫자카드input.txt", "r")

T = int(input())

if 1 <= T <= 50:
    for i in range(1, T + 1):
        N = int(input())
        N_list = list(map(int, input()))
        ln = 0
        lcmax = 0
        for k in N_list:
            lc = 0
            for z in range(N):
                if k == N_list[z]:
                    lc += 1
            if lc > lcmax:
                lcmax = lc
                ln = k
            elif lc == lcmax:
                if ln < k:
                    ln = k

        print(f'#{i} {ln} {lcmax}')

else:
    print('1에서 50 사이의 숫자를 입력해주세요.')