import sys
sys.stdin = open('0과1.txt', 'r')

from collections import deque

for tc in range(int(input())):
    n = int(input())
    visit = [-1]*n
    arr = [-1]*n
    dis = [-1]*n
    q = deque()
    q.append(1%n)
    dis[1%n] = 0
    arr[1%n] = 1
    while q:
        a = q.popleft()
        for i in range(2):
            next = (a*10+i)%n
            if dis[next] == -1:
                dis[next] = dis[a] + 1
                visit[next] = a
                arr[next] = i
                q.append(next)
    if dis[0] == -1:
        print('BRAK')
    else:
        ans = ''
        i = 0
        while i != -1:
            ans += str(arr[i])
            i = visit[i]
        print(ans[::-1])