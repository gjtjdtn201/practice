def solution(numbers, hand):
    answer = ''
    lp, rp = 10, 12
    num_list = [(1, 2, 3, 4), (2, 1, 2, 3), (3, 2, 1, 2), (4, 3, 2, 1)]
    mid_num = [2, 5, 8, 0]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            lp = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            rp = i
        else:
            idx = mid_num.index(i)
            if lp in mid_num:
                lpt = 11 if lp == 0 else lp
                lpd = num_list[(lpt-2)//3][idx]-1
            else:
                lpd = num_list[(lp-1)//3][idx]
            if rp in mid_num:
                rpt = 11 if rp == 0 else rp
                rpd = num_list[(rpt-2)//3][idx]-1
            else:
                rpd = num_list[(rp-3)//3][idx]
            if lpd == rpd:
                if hand == 'right':
                    answer += 'R'
                    rp = i
                else:
                    answer += 'L'
                    lp = i
            elif lpd < rpd:
                answer += 'L'
                lp = i
            else:
                answer += 'R'
                rp = i

    return answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers, hand))