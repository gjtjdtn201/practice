import sys
sys.stdin = open('피보나치 함수.txt')

f = [(1, 0), (0, 1)]
for i in range(2, 41):
    f.append((f[i-1][0]+f[i-2][0], f[i-1][1]+f[i-2][1]))

for tc in range(int(input())):
    print(*f[int(input())])