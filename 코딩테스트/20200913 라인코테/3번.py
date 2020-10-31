cnt = float('inf')
answer = []

def plus(first, second, depth):
    global cnt, answer
    if depth >= cnt:
        return
    case = int(first) + int(second)
    if case < 10:
        cnt = depth
        answer = [cnt, case]
        return
    test = str(case)
    for i in range(1, len(test)):
        A, B = test[:i], test[i:]
        if A[0] == '0' or B[0] == '0':
            continue
        plus(A, B, depth+1)

def solution(n):
    global cnt, answer
    if n < 10:
        answer = [0, n]
    else:
        test = str(n)
        for i in range(1, len(test)):
            first, second = test[:i], test[i:]
            if first[0] == '0' or second[0] == '0':
                continue
            plus(first, second, 1)

    return answer

n = 9
print(solution(n))