import sys
sys.stdin=open("토너먼트 카드게임.txt","r")
T = int(input())

def game(arr):
    global case, new, winner, temp, turn
    while len(arr) > 2:
        mid = (len(arr)+1)//2
        for i in range(0, mid, 2):
            case = 0
            a = arr[i]
            b = arr[i + 1] if i+1 < mid else 0
            rsp(a, b)
            if turn == 0:
                if case == 1:
                    winner.append(i)
                else:
                    winner.append(i + 1)
            else:
                if case == 1:
                    winner.append(temp[i])
                else:
                    winner.append(temp[i + 1])

        for j in range(mid, len(arr), 2):
            case = 0
            c = arr[j]
            d = arr[j+1] if j+1 < len(arr) else 0
            rsp(c,d)
            if turn == 0:
                if case == 1:
                    winner.append(j)
                else:
                    winner.append(j + 1)
            else:
                if case == 1:
                    winner.append(temp[j])
                else:
                    winner.append(temp[j+1])
        turn += 1

        arr = new
        new = []
        temp = winner
        winner = []

    #while 끝
    rsp(arr[0], arr[1])

    if case == 1:
        winner.append(temp[0])
    else:
        winner.append(temp[1])

def rsp(x,y):
    global case, new
    if y == 0:
        new.append(x)
        case = 1
    if x == 1:
        if y == 1:
            new.append(x)
            case = 1
        elif y == 2:
            new.append(y)
            case = 2
        elif y == 3:
            new.append(x)
            case = 1
    elif x == 2:
        if y == 1:
            new.append(x)
            case = 1
        elif y == 2:
            new.append(x)
            case = 1
        elif y == 3:
            new.append(y)
            case = 2
    else:
        if y == 1:
            new.append(y)
            case = 2
        elif y == 2:
            new.append(x)
            case = 1
        elif y == 3:
            new.append(x)
            case = 1

for tc in range(T):
    new = []
    winner = []
    temp = []
    N = int(input())
    group = list(map(int, input().split()))
    case = 0
    turn = 0
    game(group)
    print("#{} {}".format(tc+1,winner[0]+1))