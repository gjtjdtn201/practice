import sys
sys.stdin = open("영준이의 카드 카운팅.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    s = []
    d = []
    h = []
    c = []
    ml = input()
    ans = ''
    for i in range(0,len(ml),+3):
        b = ml[i + 1] + ml[i + 2]
        if ml[i] == 'S':
            if b in s:
                ans = 'ERROR'
                break
            s.append(b)
        elif ml[i] == 'D':
            if b in d:
                ans = 'ERROR'
                break
            d.append(b)
        elif ml[i] == 'H':
            if b in h:
                ans = 'ERROR'
                break
            h.append(b)
        elif ml[i] == 'C':
            if b in c:
                ans = 'ERROR'
                break
            c.append(b)
    if ans != 'ERROR':
        ans = f'{13-len(s)} {13-len(d)} {13-len(h)} {13-len(c)}'
    print('#{} {}'.format(test_case,ans))