import sys
sys.stdin = open('Doubles.txt', 'r')

while True:
    val = list(map(int, input().split()))
    if val[-1] == -1:
        break
    val = val[:-1]
    cnt = 0
    for i in val:
        if i / 2 in val:
            cnt += 1
    print(cnt)