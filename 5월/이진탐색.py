for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    answer = 0
    for i in B:
        lo = 0
        hi = N-1
        chk = 0
        while lo <= hi:
            mid = (lo+hi)//2
            if i == A[mid]:
                answer += 1
                break
            if i >= A[mid]:
                lo = mid + 1
                if chk == 1:
                    break
                chk = 1
            else:
                hi = mid - 1
                if chk == -1:
                    break
                chk = -1
    print('#{} {}'.format(tc, answer))
