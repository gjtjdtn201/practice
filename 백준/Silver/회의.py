import sys
sys.stdin = open('회의.txt')

import sys
input = sys.stdin.readline
N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x:(x[1], x[0]))
end = answer = 0
for i in meeting:
    if end <= i[0]:
        end = i[1]
        answer += 1
print(answer)