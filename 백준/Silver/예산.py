import sys
sys.stdin = open('예산.txt')

N = int(input())
A = list(map(int, input().split()))
M = int(input())

# 시작값 0으로 두자!
st, ed = 0, max(A)
cnt = 0
while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in A:
        cnt += i if i < mid else mid
    if cnt <= M:
        st = mid+1
    else:
        ed = mid-1
print(st-1)