from collections import deque

def solution(board, r, c):
    ans = [[] for _ in range(6)]
    max_val = 0
    answer = 0
    for y in range(4):
        for x in range(4):
            if board[y][x] > 0:
                max_val = max(board[y][x], max_val)
                ans[board[y][x]].append((y, x))
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    q = deque()
    q.append((r, c))
    while q:
        a, b = q.popleft()
        if board[a][b] == 0:
            for i in range(4):
                chk = 0
                ny = a + dy[i]
                nx = b + dx[i]
                while 0 <= ny < 4 and 0 <= nx < 4:
                    if board[ny][nx] > 0:
                        chk = 1
                        break
                    ny += dy[i]
                    nx += dx[i]
                if chk:
                    answer += 1
                    if ans[board[ny][nx]][0] == (ny, nx):
                        target = ans[board[ny][nx]][1]
                    else:
                        target = ans[board[ny][nx]][0]
                    if target[0] == ny or target[1] == nx:
                        answer += 1
                    else:
                        answer += 2
                    q.append(target)
                    ans[board[ny][nx]] = []
                    board[ny][nx] = 0
                    board[target[0]][target[1]] = 0
                    break
            else:
                for z in range(6):
                    if ans[z]:
                        answer += 2
                        target = ans[z][1]
                        if target[0] == ans[z][0] or target[1] == ans[z][1]:
                            answer += 1
                        else:
                            answer += 2
                        q.append(target)
                        board[target[0]][target[1]] = 0
                        board[ans[z][0][0]][ans[z][0][1]] = 0
                        ans[z] = []
                        break
        else:
            if ans[board[a][b]][0] == (a, b):
                target = ans[board[a][b]][1]
            else:
                target = ans[board[a][b]][0]
            if target[0] == a or target[1] == b:
                answer += 1
            else:
                answer += 2
            q.append(target)
            ans[board[a][b]] = []
            board[a][b] = 0
            board[target[0]][target[1]] = 0



    answer += max_val*2
    return answer

board, r, c = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1
print(solution(board, r, c))