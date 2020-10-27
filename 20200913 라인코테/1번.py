def solution(boxes):
    ans = 0
    box = []
    val = len(boxes)
    for i in boxes:
        box.extend(i)
    box.sort()
    cnt = 0
    for i in box:
        if i == cnt:
            ans += 1
            cnt = 0
        cnt = i
    ans = val - ans
    return ans

boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]

print(solution(boxes))