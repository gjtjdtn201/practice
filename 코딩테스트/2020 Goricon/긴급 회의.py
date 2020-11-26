import sys
sys.stdin = open('긴급 회의.txt')

N = int(input())
vote = list(map(int, input().split()))
ans = [0]*N
for i in vote:
    if i == 0:
        continue
    ans[i-1] += 1
res = 0
chk = 0
for i in range(1, N):
    if ans[i] > ans[res]:
        res = i
        chk = 0
    elif ans[i] == ans[res]:
        chk = 1
print('skipped' if chk else res+1)