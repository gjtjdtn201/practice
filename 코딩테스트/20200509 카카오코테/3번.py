def solution(gems):
    target = list(set(gems))
    N = len(gems)
    M = len(target)
    ngems = [0]*M
    lo = hi = 0
    ans = N
    answer = [1, N]
    while True:
        if ngems.count(0) == 0:
            idx = target.index(gems[lo])
            ngems[idx] -= 1
            lo += 1
        elif hi == N:
            break
        else:
            idx = target.index(gems[hi])
            ngems[idx] += 1
            hi += 1
        if ngems.count(0) == 0:
            if ans > hi -lo:
                answer = [lo+1, hi]
                ans = hi-lo

    return answer

a = ["XYZ", "XYZ", "XYZ"]
print(solution(a))