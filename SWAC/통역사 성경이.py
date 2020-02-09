import sys
sys.stdin = open("통역사 성경이.txt", 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    word = input()
    cnt = 0
    i = 0
    ans = []
    while i < len(word):
        if word[i].isupper():
            chk = 0
            for x in range(i+1,len(word)):
                if word[x] == ' ':
                    if chk == 1:
                        cnt -= 1
                    cnt += 1
                    i = x
                    break
                elif word[x].isupper() or word[x].isdecimal():
                    chk = 1
                elif word[x] == '!' or word[x] == '.' or word[x] == '?':
                    if chk == 1:
                        cnt -= 1
                    cnt += 1
                    ans.append(cnt)
                    cnt = 0
                    i = x
                    break
        elif word[i] == '!' or word[i] == '.' or word[i] == '?':
            ans.append(cnt)
            cnt = 0
        i += 1
    b = ''
    for i in ans:
        b += str(i) + ' '
    print('#{} {}'.format(test_case, b.rstrip()))