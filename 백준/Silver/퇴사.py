import sys
sys.stdin = open('퇴사.txt', 'r')

def score():
    cnt = 0
    for i in range(N):
        if A[i] == 1:
            cnt += pay[i]
    return cnt

def DC(k, days):
    global ans
    if k < N and day[k] < N:
        A[k] = 1        # k번 요소 O
        DC(k + day[k], days + day[k])  # 다음 요소 포함 여부 결정
        A[k] = 0        # k번 요소 X
        DC(k + 1, days)  # 다음 요소 포함 여부 결정
    else:
        z = score()
        if z > ans:
            ans = z

N = int(input())
day = []
pay = []
for i in range(N):
    a, b = map(int, input().split())
    day.append(a)
    pay.append(b)
A = [0 for _ in range(N)]  # 원소의 포함여부 저장 (0, 1)
ans = 0
DC(0, 0)

print(ans)