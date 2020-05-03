import sys
sys.stdin = open('숨바꼭질 3.txt')

def find(K):
    q = [(N, 0)]
    cnt = 1
    while True:
        qtmp = []
        for a, b in q:
            if a == K:
                print(b)
                return
            for nxt in [a+1, a-1, a*2]:
                if 0 <= nxt < PG:
                    qtmp.append((nxt, b+1))
        K += cnt
        if K >= PG:
            print(-1)
            return
        cnt += 1
        if not qtmp:
            break
        q = qtmp
    print(-1)

N, K = map(int, input().split())
PG = 500001
find(K)
