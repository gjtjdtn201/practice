import sys
sys.stdin = open('퇴사.txt', 'r')

def DC(n, k, days):
    global ans
    #####################################
    if days > n or k > n:
        return
    #####################################
    if n == k:  # Basis Part
        cnt = 0
        for i in range(N):
            if A[i] == 1:
                cnt += pay[i]
        if cnt > ans:
            ans = cnt
    elif k < n:
        A[k] = 1  # k번 요소 O
        DC(n, k + day[k], days + day[k])  # 다음 요소 포함 여부 결정
        A[k] = 0  # k번 요소 X
        DC(n, k + 1, days)  # 다음 요소 포함 여부 결정
    else:
        A[k] = 0  # k번 요소 X
        DC(n, k + 1, days)  # 다음 요소 포함 여부 결정
N = int(input())
day = []
pay = []
for i in range(N):
    a, b = map(int, input().split())
    day.append(a)
    pay.append(b)
A = [0 for _ in range(N)]  # 원소의 포함여부 저장 (0, 1)
ans = 0
DC(N, 0, 0)

print(ans)