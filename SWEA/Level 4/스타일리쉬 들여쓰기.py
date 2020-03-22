import sys
sys.stdin = open('스타일리쉬 들여쓰기.txt', 'r')

def A_F(code, I):
    global af
    ab = cd = ef = 0
    for i in range(I):
        for j in range(len(code[i])):
            if code[i][j] == '(':
                ab += 1
            elif code[i][j] == ')':
                ab -= 1
            elif code[i][j] == '{':
                cd += 1
            elif code[i][j] == '}':
                cd -= 1
            elif code[i][j] == '[':
                ef += 1
            elif code[i][j] == ']':
                ef -= 1
        af.append((ab, cd, ef))

def RCS(af, indenp, p):
    org = []
    ab, cd, ef = af[0]
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:
                    org.append((R,C,S))
                elif R*ab + C*cd + S*ef == indenp[1]:
                    org.append((R, C, S))
    for i in range(2, p):
        ab, cd, ef = af[i-1]
        dest = []
        for R, C, S in org:
            if R*ab + C*cd + S*ef == indenp[i]:
                dest.append((R, C, S))
        org = dest
    return org

for tc in range(1, int(input())+1):
    p, q = map(int, input().split())
    indenp = [0] * p
    codep = []
    codeq = []

    for i in range(p):
        codep.append(input())
    for i in range(q):
        codeq.append(input())

    af = []
    A_F(codep, p)

    for i in range(p):
        cnt = 0
        while codep[i][cnt] == '.':
            cnt += 1
        indenp[i] = cnt

    # R, C, S 후보 정하기
    rcs = RCS(af, indenp, p)

    af = []
    A_F(codeq, q)
    indenq = [0] * q
    for i in range(1, q):
        ab, cd, ef = af[i-1]
        if rcs:
            R, C, S = rcs[0]
            ans = R*ab + C*cd + S*ef
            for x in rcs[1:]:
                R, C, S = x
                if R*ab + C *cd + S * ef != ans:
                    indenq[i] = -1
                    break
            if indenq[i] != -1:
                indenq[i] = ans
        else:
            indenq[i] = -1
            break
    print('#{} '.format(tc), end='')
    print(*indenq)