def solution(maze):
    N = len(maze)
    answer = 0
    stack = []
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    if maze[0][1] == 0:
        start = 0
        wy = -1
        wx = 0
    else:
        start = 1
        wy = 0
        wx = 1
    stack.append((0, 0, 0, start, wy, wx))
    while stack:
        chk = 0
        a, b, c, start, wy, wx = stack.pop()
        print(a, b, c)
        ny = a + dy[start]
        nx = b + dx[start]
        wy = wy + dy[start]
        wx = wx + dx[start]
        if 0 <= wy < N and 0 <= wx <= N and maze[wy][wx] == 0:
            chk = 1
            wy = wy - dy[start]
            wx = wx - dx[start]
            start -= 1
            if start < 0:
                start = 3

        if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] == 0:
            if (ny, nx) == (N - 1, N - 1):
                answer = c + 1
                break
            stack.append((ny, nx, c + 1, start, wy, wx))
            continue
        else:
            if chk:
                stack.append((a, b, c, start, wy, wx))
            else:
                start += 1
                if start > 3:
                    start = 0
                stack.append((a, b, c, start, ny, nx))


    return answer

maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
print(solution(maze))