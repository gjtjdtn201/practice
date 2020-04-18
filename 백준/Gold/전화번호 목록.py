import sys
sys.stdin = open('전화번호 목록.txt')

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    a = [input().rstrip() for _ in range(int(input()))]
    a.sort()
    for i in range(len(a)-1):
        if a[i] in a[i+1][:len(a[i])]:
            print('NO')
            break
    else:
        print('YES')