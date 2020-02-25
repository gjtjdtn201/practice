import sys
sys.stdin = open('텀 프로젝트.txt', 'r')
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    n = int(input())
    al = [0] + list(map(int, input().split()))

    visit = [0] * (n + 1)
    cnt = n
    for i in range(1, n+1):
        if not visit[i]:
            group = []
            stack = [i]
            while stack:
                num = stack.pop()
                visit[num] = 1
                group.append(num)
                if visit[al[num]] == 0:
                    stack.append(al[num])
                    continue
                elif num == al[num]:
                    cnt -= 1
                    break
                else:
                    try:
                        cnt -= len(group) - group.index(al[num])
                    except ValueError:
                        break
    print(cnt)
