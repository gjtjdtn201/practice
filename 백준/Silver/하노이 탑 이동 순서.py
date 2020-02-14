T = int(input())

def Hanoy(N, one, two, three):
    if N == 1:
        print('{} {}'.format(one,three))
        return
    Hanoy(N-1, one, three, two)
    print('{} {}'.format(one, three))
    Hanoy(N-1, two, one, three)

print(2**T-1)
Hanoy(T,1,2,3)