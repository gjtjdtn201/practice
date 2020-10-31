def solution(encrypted_text, key, rotation):
    answer = ''
    rotation = rotation % len(key)
    if rotation < 0:
        rotation = len(key) + rotation
    BeforeRotation = encrypted_text[rotation:] + encrypted_text[:rotation]
    print(BeforeRotation)
    # ord('a') = 97, chr(97) = 'a'
    for i in range(len(BeforeRotation)):
        num = ord(BeforeRotation[i]) - (ord(key[i]) - 96)
        if num < 97:
            num = 123 - (97 - num)
        answer += chr(num)

    return answer