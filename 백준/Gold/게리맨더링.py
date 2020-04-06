import sys
sys.stdin = open('게리맨더링.txt', 'r')

from itertools import combinations

def dfs(val, visit):
    stack = [val]
    while stack:
        n = stack.pop()
        visit[n] = 1
        for z in tree[n]:
            if visit[z] == 0:
                stack.append(z)
    return visit

N = int(input())

people = list(map(int, input().split()))
tree = [[] for _ in range(N+1)]

cnt = 0
ans = 9999
chk = chk2 = chk3 = 0
for i in range(1, N+1):
    line = list(map(int, input().split()))
    tree[i].extend(line[1:])
    if line[0] == 0:
        cnt += 1
        al = i
if N == 2:
    ans = abs(sum(people) - people[0]*2)
elif cnt > 1:
    ans = -1
elif cnt == 1:
    ans = abs(sum(people) - people[al-1]*2)
else:
    for i in range(N//2, 0, -1):
        a = list(combinations(range(1, N+1), i))
        for j in a:
            chk = 0
            cnt1 = 0
            vis = [0] * (N + 1)
            vis2 = vis[:]
            num = list(range(1, N + 1))
            for r in j:
                vis2[r] = 2
                num.remove(r)
            for t in num:
                vis[t] = 2
            sc = dfs(j[0], vis)
            for x in j:
                if sc[x] != 1:
                    chk = 1
                    break
            if chk == 1:
                continue
            sc = dfs(num[0], vis2)
            for w in num:
                cnt1 += people[w-1]
                if sc[w] != 1:
                    chk = 1
                    break
            if chk == 1:
                continue
            cnt = abs(sum(people) - cnt1*2)
            chk2 = 1
            if cnt == 0:
                ans = 0
                chk3 = 1
                break
            if ans > cnt:
                ans = cnt
        if chk3 == 1:
            break
    if chk2 == 0:
        ans = -1
print(ans)