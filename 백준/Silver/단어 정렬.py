import sys
sys.stdin = open('단어 정렬.txt', 'r')

T = int(input())
words = set()
for i in range(T):
    word = input()
    words.add((len(word),word))
for i in sorted(words, key= lambda x : (x[0], x[1])):
    print(i[1])