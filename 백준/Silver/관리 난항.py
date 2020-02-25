import sys
sys.stdin = open('관리 난항.txt', 'r')

from math import ceil

T = int(input())

for test_case in range(T):
    n, m = map(int, input().split())
    rent = []
    for i in range(n):
        N, p, q, k = list(input().split())
        rent.append([N, int(p), int(q), int(k)])

    name = []
    ans = []
    chk = 0
    for i in range(m):
        t, S, e, zz = list(input().split())
        for pp in ans:
            if pp[0] == S and pp[1] == 'INCONSISTENT':
                chk = 1
                break
        if chk == 1:
            chk = 0
            continue

        elif e == 'p':
            for hh in name:
                if hh[0] == S:
                    chk = 1
                    break
            else:
                for jj in rent:
                    if jj[0] == zz:
                        name.append([S, jj[1], jj[2], jj[3], 0])
        elif e == 'r':
            for ii in name:
                if ii[0] == S:
                    ii[4] += int(zz) * ii[3] + ii[2]
                    ans.append([S, ceil(ii[4])])
                    name.remove(ii)
                    break
            else:
                for bb in ans:
                    if S == bb[0]:
                        ans.remove(bb)
                ans.append([S, 'INCONSISTENT'])
        elif e == 'a':
            for kk in name:
                if kk[0] == S:
                    kk[4] += kk[1] * (int(zz) / 100)
                    break
            else:
                for bb in ans:
                    if S == bb[0]:
                        ans.remove(bb)
                ans.append([S, 'INCONSISTENT'])
    for i in name:
        for z in ans:
            if i[0] == z[0]:
                ans.remove(z)
        ans.append([i[0], 'INCONSISTENT'])
    ans.sort()
    for i in ans:
        print(*i)