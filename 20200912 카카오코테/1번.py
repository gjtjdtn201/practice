def solution(new_id):
    step1 = new_id.lower()
    step2 = ''
    eng = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    flag = False
    for i in step1:
        if i in eng or i in num or i == '-' or i == '_' or i == '.':
            if i == '.' and flag:
                continue
            elif i == '.':
                flag = True
            else:
                flag = False
            step2 += i
    if step2[0] == '.':
        step2 = step2[1:]
    try:
        if step2[-1] == '.':
            step2 = step2[:-1]
    except:
        pass
    if step2 == '':
        step2 = 'a'
    if len(step2) >= 16:
        step2 = step2[:15]
    if step2[-1] == '.':
        step2 = step2[:-1]
    while len(step2) <= 2:
        step2 += step2[-1]

    answer = step2
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."	"z--"))
print(solution("=.="	"aaa"))
print(solution("123_.def"	"123_.def"))
print(solution("abcdefghijklmn.p"))
