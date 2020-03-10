import sys
sys.stdin = open('자기 방으로 돌아가기.txt', 'r')

for t in range(1, int(input())+1):
    v = [0] * 201
    for i in range(int(input())):
        p, g = map(int, input().split())
        if p > g:
            p, g = g, p
        for j in range(int(p/2+0.5), int(g/2+0.5)+1):
            v[j] += 1
    print('#{} {}'.format(t, max(v)))