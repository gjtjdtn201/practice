import sys
sys.stdin = open('123.txt')

N, C = map(int, input().split())

house = []
for i in range(N):
    house.append(int(input()))
house.sort()
print(house)
start, end = house[1] - house[0], house[-1] - house[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    cur_house = house[0]
    count = 1
    for i in range(1, N):
        if house[i] >= cur_house + mid:
            count += 1
            cur_house = house[i]
    if count >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)