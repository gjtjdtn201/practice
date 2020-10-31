def solution(n, delivery):
    answer = ''
    N = [0]*(n+1)
    for A, B, C in delivery:
        if C:
            N[A], N[B] = 1, 1
    for A, B, C in delivery:
        if N[A] + N[B] == 1 and C == 0:
            if N[A] == 0:
                N[A] = 2
            else:
                N[B] = 2
    for i in range(1, n+1):
        if N[i] == 0:
            answer += '?'
        elif N[i] == 1:
            answer += 'O'
        else:
            answer += 'X'
    return answer