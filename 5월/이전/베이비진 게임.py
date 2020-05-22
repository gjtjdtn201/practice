import sys
sys.stdin = open('베이비진 게임.txt')

def perm(a, n, r, k):
    global chk
    if chk == 1:
        return
    if r == k:
        if t[0] == t[1] == t[2]:
            chk = 1
        elif t[0]+2 == t[1]+1 == t[2]:
            chk = 1
        elif t[0] == t[1]+1 == t[2]+2:
            chk = 1
        return
    else:
        for i in range(0, n):
            if chk == 1: return
            if visited[i]: continue
            t[k] = a[i]
            visited[i] = True
            perm(a, n, r, k + 1)
            visited[i] = False

for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    p1, p2 = [cards[0], cards[2]], [cards[1], cards[3]]
    chk = 0
    ans = 0
    t = [0] * 3
    for i in range(4, 12):
        if not i&1:
            p1.append(cards[i])
            visited = [0]*(i//2+1)
            perm(p1, i//2+1, 3, 0)
        else:
            p2.append(cards[i])
            visited = [0]*(i//2+1)
            perm(p2, i//2+1, 3, 0)
        if chk == 1:
            ans = 2 if i&1 else 1
            break
    print('#{} {}'.format(tc, ans))