def solution(encrypted_text, key, rotation):
    answer = ''
    word = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
            11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
            20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
           'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
           't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    temp = list(encrypted_text)
    ttemp = ['' for _ in range(len(encrypted_text))]

    # 문자를 반대로 돌립니다.
    for w in range(len(temp)):
        r = abs(rotation) % len(temp)
        if rotation > 0:
            n_i = w - r
            if n_i < 0:
                n_i = len(temp) + n_i
        else:
            n_i = w + r
            if n_i > len(temp) - 1:
                n_i = 0 + (n_i - len(temp))
        ttemp[n_i] = temp[w]
    temp = [w for w in ttemp]

    # key 값을 이용한 암호화를 해제합니다.
    for w in range(len(temp)):
        e_w = num[temp[w]]
        k_w = num[key[w]]
        r = e_w - k_w
        if r < 1:
            r = 26 + r
        elif r > 26:
            r = r - 26
        temp[w] = word[r]
    answer = ''.join(temp)
    return answer
A = 'abcdefghijklmnopqrstuvwxyz'*26
B = ''
for i in range(26):
    B += chr(i+97)*26
C = 0
print(solution(A, B, C))