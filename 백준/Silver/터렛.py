import sys
sys.stdin = open('터렛.txt')

for tc in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if (x1, y1) == (x2, y2):
        print(-1 if r1 == r2 else 0)
    elif dist+r1 > r2 and dist+r2 > r1 and r1+r2 > dist:
        print(2)
    # 내접하거나 외접할때
    elif dist+r1 == r2 or dist+r2 == r1 or r1+r2 == dist:
        print(1)
    else:
        print(0)