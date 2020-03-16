import sys
sys.stdin = open('상호의 배틀 필드.txt', 'r')


from collections import deque

def SC():
    for y in range(H):
        for x in range(W):
            if matrix[y][x] in tank:
                return y, x


for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    N = int(input())
    move = deque(input())
    tank = ['<', '^', '>', 'v']
    sty, stx = SC()

    while move:
        ac = move.popleft()
        if ac == 'U':
            if 0 <= sty-1 and matrix[sty-1][stx] == '.':
                matrix[sty-1][stx] = '^'
                matrix[sty][stx] = '.'
                sty, stx = sty-1, stx
            else:
                matrix[sty][stx] = '^'
        elif ac == 'D':
            if sty+1 < H and matrix[sty+1][stx] == '.':
                matrix[sty+1][stx] = 'v'
                matrix[sty][stx] = '.'
                sty, stx = sty+1, stx
            else:
                matrix[sty][stx] = 'v'
        elif ac == 'L':
            if 0 <= stx-1 and matrix[sty][stx-1] == '.':
                matrix[sty][stx-1] = '<'
                matrix[sty][stx] = '.'
                sty, stx = sty, stx-1
            else:
                matrix[sty][stx] = '<'
        elif ac == 'R':
            if stx+1 < W and matrix[sty][stx+1] == '.':
                matrix[sty][stx+1] = '>'
                matrix[sty][stx] = '.'
                sty, stx = sty, stx+1
            else:
                matrix[sty][stx] = '>'
        elif ac == 'S':
            if matrix[sty][stx] == '<':
                for i in range(stx, -1, -1):
                    if matrix[sty][i] == '*':
                        matrix[sty][i] = '.'
                        break
                    elif matrix[sty][i] == '#':
                        break
            elif matrix[sty][stx] == '^':
                for i in range(sty, -1, -1):
                    if matrix[i][stx] == '*':
                        matrix[i][stx] = '.'
                        break
                    elif matrix[i][stx] == '#':
                        break
            elif matrix[sty][stx] == '>':
                for i in range(stx, W):
                    if matrix[sty][i] == '*':
                        matrix[sty][i] = '.'
                        break
                    elif matrix[sty][i] == '#':
                        break
            elif matrix[sty][stx] == 'v':
                for i in range(sty, H):
                    if matrix[i][stx] == '*':
                        matrix[i][stx] = '.'
                        break
                    elif matrix[i][stx] == '#':
                        break

    print('#{} '.format(tc), end='')
    for i in matrix:
        print(''.join(i))