from collections import deque

def solution(cards):
    answer = 0
    q = deque()
    q.extend(cards)
    while len(q) > 3:
        dealer = []
        player = []
        for z in range(2):
            card = q.popleft()
            if card > 10:
                card = 10
            player.append(card)
            card = q.popleft()
            if card > 10:
                card = 10
            dealer.append(card)
        phand = 0
        for i in player:
            if i == 1:

            phand += i
        if dealer[1] == 1 or dealer[1] == 7:


    return answer

cards = [12, 7, 11, 6, 2, 12]
print(solution(cards))