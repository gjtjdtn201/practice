import sys
sys.stdin = open('나는 개구리로소이다.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    word = list(input())
    chk = []
    ans = cnt = 0
    if len(word) % 5:
        ans = -1
    else:
        for i in word:
            if i == 'c':
                chk.append(['c'])
                if ans < len(chk):
                    ans = len(chk)
            elif i == 'r':
                for j in range(len(chk)):
                    if len(chk[j]) == 1:
                        chk[j].append(i)
                        break
                else:
                    cnt = 1
                    break
            elif i == 'o':
                for j in range(len(chk)):
                    if len(chk[j]) == 2:
                        chk[j].append(i)
                        break
                else:
                    cnt = 1
                    break
            elif i == 'a':
                for j in range(len(chk)):
                    if len(chk[j]) == 3:
                        chk[j].append(i)
                        break
                else:
                    cnt = 1
                    break
            elif i == 'k':
                for j in range(len(chk)):
                    if len(chk[j]) == 4:
                        del chk[j]
                        break
                else:
                    cnt = 1
                    break
            else:
                ans = -1
                break
        if cnt == 1 or len(chk) != 0:
            ans = -1

    print('#{} {}'.format(test_case, ans))