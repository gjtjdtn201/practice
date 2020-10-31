from itertools import combinations

def solution(orders, course):
    answer = []
    c = set()
    max_len = 0
    for i in orders:
        c.update(list(i))
        max_len = max(max_len, len(i))
    c = sorted(list(c))

    for cnt in course:
        ans = []
        if cnt > max_len:
            break
        least = 2
        for z in combinations(c, cnt):
            cnt = 0
            for i in orders:
                for j in z:
                    if j not in i:
                        break
                else:
                    cnt += 1
            if least == cnt:
                ans.append(''.join(z))
            elif least < cnt:
                ans = []
                ans.append(''.join(z))
                least = cnt
        answer.extend(ans)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))