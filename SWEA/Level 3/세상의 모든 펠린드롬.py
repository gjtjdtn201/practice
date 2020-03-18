import sys
sys.stdin = open('세상의 모든 펠린드롬.txt', 'r')

for tc in range(1, int(input())+1):
    a = input()
    print('#{} '.format(tc), end='')
    for i in range(len(a)//2):
        if a[i] == a[-i-1] or a[i] == '?' or a[-1-i] == '?':
            continue
        else:
            print('Not exist')
            break
    else:
        print('Exist')
