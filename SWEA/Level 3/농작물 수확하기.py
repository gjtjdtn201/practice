import sys
sys.stdin = open('농작물 수확하기.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    ans = 0
    mid = N//2
    for i in range(N):
        a = list(map(int, input()))
        s = i
        if i >= mid:
            s = 2*mid - i
        ans += sum(a[mid-s:mid+s+1])

    print('#{} {}'.format(tc, ans))