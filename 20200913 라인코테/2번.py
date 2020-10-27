from collections import deque

def solution(ball, order):
    answer = []
    q = deque()
    q.extend(ball)
    stash = []
    for step in order:
        if q[0] == step:
            q.popleft()
            answer.append(step)
        elif q[-1] == step:
            q.pop()
            answer.append(step)
        else:
            stash.append(step)
            continue
        if stash:
            chk = 1
            while chk:
                chk = 0
                for i in stash:
                    if q[0] == i:
                        q.popleft()
                        answer.append(i)
                        chk = 1
                    elif q[-1] == i:
                        q.pop()
                        answer.append(i)
                        chk = 1
                    if chk:
                        stash.remove(i)

    return answer

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]
print(solution(ball, order))