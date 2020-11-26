import sys
sys.stdin = open('게임.txt')

X, Y = map(int, input().split())

Z = int(100*Y/X)
if X == Y:
    print(-1)
else:
    start, ans = 0, -1
    end = 1000000000
    while start <= end:
        mid = (start+end)//2
        if Z < int(100*(Y + mid)/(X + mid)):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    print(ans)